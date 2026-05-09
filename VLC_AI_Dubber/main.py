import os
import time
import hashlib
import threading
import urllib.parse
import urllib.request
import re
import asyncio

import requests
import pygame
import pysubs2
from google.cloud import texttospeech
import edge_tts

import config

# ==========================================
# 1. GIAO TIẾP VỚI VLC (VLC Controller)
# ==========================================
class VLCController:
    def __init__(self):
        self.host = config.VLC_HOST
        self.port = config.VLC_PORT
        self.session = requests.Session()
        self.session.auth = ('', config.VLC_PASSWORD)
    
    def get_status(self):
        try:
            url = f"http://{self.host}:{self.port}/requests/status.json"
            response = self.session.get(url, timeout=1)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def set_volume(self, level):
        try:
            url = f"http://{self.host}:{self.port}/requests/status.json?command=volume&val={level}"
            self.session.get(url, timeout=1)
        except:
            pass

    def get_current_video_path(self):
        r"""Tuyệt chiêu: Lấy đường dẫn TUYỆT ĐỐI của file đang phát (D:\...)"""
        try:
            url = f"http://{self.host}:{self.port}/requests/playlist.json"
            response = self.session.get(url, timeout=1)
            if response.status_code == 200:
                data = response.json()
                
                # Quét playlist tìm file đang chiếu (current)
                def find_current(nodes):
                    for node in nodes:
                        if node.get("current") == "current":
                            return node.get("uri")
                        if "children" in node:
                            res = find_current(node["children"])
                            if res: return res
                    return None
                
                uri = find_current(data.get("children", []))
                if uri:
                    # Chuyển đổi file:///D:/... thành đường dẫn chuẩn Windows
                    parsed_url = urllib.parse.urlparse(uri)
                    real_path = urllib.request.url2pathname(parsed_url.path)
                    return real_path
        except:
            pass
        return None

# ==========================================
# 2. XỬ LÝ PHỤ ĐỀ (Subtitle Manager)
# ==========================================
class SubtitleManager:
    @staticmethod
    def get_ass_path(video_path):
        base_name = os.path.splitext(video_path)[0]
        return base_name + ".ass"

    @staticmethod
    def load_subtitles(ass_path):
        if not os.path.exists(ass_path):
            print(f"[!] Không tìm thấy file sub tại: {ass_path}")
            return []
        
        print(f"\n[+] ĐÃ TÌM THẤY PHỤ ĐỀ: {ass_path}")
        subs = pysubs2.load(ass_path, encoding="utf-8")
        clean_subs = []
        
        for line in subs:
            # Loại bỏ tag ASS {...} và ký tự xuống dòng
            text = re.sub(r'\{.*?\}', '', line.text)
            text = text.replace('\\N', ' ').replace('\\n', ' ').strip()
            
            if text and len(text) > 0:
                clean_subs.append({
                    "start": line.start,
                    "end": line.end,
                    "text": text,
                    "actor": line.name
                })
        return clean_subs

# ==========================================
# 3. XỬ LÝ ÂM THANH AI (Voice Engine)
# ==========================================
class EdgeVoiceEngine:
    def __init__(self):
        if not os.path.exists(config.CACHE_DIR):
            os.makedirs(config.CACHE_DIR)

    def get_hash(self, text, voice):
        chuoi_can_hash = text + "_" + voice
        return hashlib.md5(chuoi_can_hash.encode('utf-8')).hexdigest()

    async def _generate_async(self, text, voice_name, rate, file_path):
        communicate = edge_tts.Communicate(text, voice_name, rate=rate)
        await communicate.save(file_path)

    def generate_audio(self, text, voice_name=config.EDGE_VOICE):
        if not text or not text.strip():
            return None

        hash_id = self.get_hash(text, voice_name)
        file_path = os.path.join(config.CACHE_DIR, f"{hash_id}.mp3")
        
        if os.path.exists(file_path):
            return file_path 

        try:
            # In log để debug nếu cần
            # print(f"[*] Đang tạo Edge TTS cho: {text[:30]}...")
            asyncio.run(self._generate_async(text, voice_name, config.EDGE_RATE, file_path))
            return file_path
        except Exception as e:
            if "No audio was received" in str(e):
                print(f"[!] Edge TTS: Không nhận được âm thanh cho văn bản: '{text}'")
            else:
                print(f"[!] Lỗi Edge TTS API: {e} | Text: {text}")
            return None

class GoogleVoiceEngine:
    def __init__(self):
        if not os.path.exists(config.CACHE_DIR):
            os.makedirs(config.CACHE_DIR)
        self.client = texttospeech.TextToSpeechClient()

    def get_hash(self, text, voice):
        chuoi_can_hash = text + "_" + voice
        return hashlib.md5(chuoi_can_hash.encode('utf-8')).hexdigest()

    def generate_audio(self, text, voice_name=config.GOOGLE_VOICE):
        hash_id = self.get_hash(text, voice_name)
        file_path = os.path.join(config.CACHE_DIR, f"{hash_id}.mp3")
        
        if os.path.exists(file_path):
            return file_path 

        try:
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(language_code="vi-VN", name=voice_name)
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=config.SPEAKING_RATE
            )
            response = self.client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            with open(file_path, "wb") as out:
                out.write(response.audio_content)
            return file_path
        except Exception as e:
            print(f"[!] Lỗi Google API: {e}")
            return None

class VoiceEngineWrapper:
    def __init__(self):
        self.engine_type = config.TTS_ENGINE
        if self.engine_type == "EDGE":
            print("[+] Khởi tạo Edge TTS Engine (Nhanh & Miễn phí)")
            self.engine = EdgeVoiceEngine()
        else:
            print("[+] Khởi tạo Google Cloud TTS Engine")
            self.engine = GoogleVoiceEngine()

    def generate_audio(self, text):
        return self.engine.generate_audio(text)

from concurrent.futures import ThreadPoolExecutor

# ==========================================
# 4. CHƯƠNG TRÌNH CHÍNH (Dubbing Daemon)
# ==========================================
class DubbingDaemon:
    def __init__(self):
        self.vlc = VLCController()
        self.tts = VoiceEngineWrapper()
        pygame.mixer.init()
        
        self.current_video = None
        self.subtitles = []
        self.last_played_idx = -1
        self.is_ducking = False
        self.executor = ThreadPoolExecutor(max_workers=5) # Cho phép tải 5 câu cùng lúc
        self.stop_prefetch = threading.Event()

    def smart_prefetch(self, current_time_ms):
        """Ưu tiên tải N câu tiếp theo một cách song song."""
        start_idx = 0
        for i, sub in enumerate(self.subtitles):
            if sub['end'] >= current_time_ms:
                start_idx = i
                break
        
        end_idx = min(start_idx + config.PREFETCH_COUNT, len(self.subtitles))
        
        # Gửi các tác vụ tải vào ThreadPool để chạy song song
        for i in range(start_idx, end_idx):
            if self.stop_prefetch.is_set():
                break
            text = self.subtitles[i]['text']
            # Kiểm tra xem đã có trong cache chưa trước khi gửi vào thread
            self.executor.submit(self.tts.generate_audio, text)

    def run(self):
        print("🚀 [AI-VoxSync Daemon] Chế độ Tải Song Song đã kích hoạt!")
        last_time_ms = 0


        while True:
            time.sleep(0.05) 
            
            status = self.vlc.get_status()
            if not status or 'information' not in status:
                continue

            if status.get('state') != 'playing':
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                continue
            else:
                pygame.mixer.music.unpause()

            video_path = self.vlc.get_current_video_path()
            if not video_path:
                continue

            current_time_ms = int(status['time'] * 1000)

            # Phim mới hoặc phim bị thay đổi
            if video_path != self.current_video:
                self.current_video = video_path
                ass_path = SubtitleManager.get_ass_path(video_path)
                self.subtitles = SubtitleManager.load_subtitles(ass_path)
                self.last_played_idx = -1
                last_time_ms = 0
                
                # Dừng luồng tải cũ nếu có
                self.stop_prefetch.set()
                if self.prefetch_thread:
                    self.prefetch_thread.join(timeout=1)
                
                if self.subtitles:
                    self.stop_prefetch.clear()
                    self.prefetch_thread = threading.Thread(target=self.smart_prefetch, args=(current_time_ms,), daemon=True)
                    self.prefetch_thread.start()

            # Phát hiện tua phim (seek) - nếu thời gian nhảy vọt (vd: > 5s)
            if abs(current_time_ms - last_time_ms) > 5000 and self.subtitles:
                 print(f"[*] Tua phim phát hiện. Bắt đầu pre-fetch từ {current_time_ms/1000}s...")
                 self.stop_prefetch.set()
                 if self.prefetch_thread:
                    self.prefetch_thread.join(timeout=1)
                 self.stop_prefetch.clear()
                 self.prefetch_thread = threading.Thread(target=self.smart_prefetch, args=(current_time_ms,), daemon=True)
                 self.prefetch_thread.start()

            last_time_ms = current_time_ms

            if not self.subtitles:
                continue

            # ĐỒNG BỘ THỜI GIAN
            sub_is_active = False

            for i, sub in enumerate(self.subtitles):
                if sub['start'] <= current_time_ms <= sub['end']:
                    sub_is_active = True
                    
                    if self.last_played_idx != i:
                        audio_path = self.tts.generate_audio(sub['text'])
                        
                        if audio_path and os.path.exists(audio_path):
                            pygame.mixer.music.load(audio_path)
                            pygame.mixer.music.play()
                            print(f"🎙️ AI [{config.TTS_ENGINE}]: {sub['text']}")
                            
                            self.vlc.set_volume(config.VOLUME_DUCKING)
                            self.is_ducking = True
                            
                        self.last_played_idx = i
                    break
            
            if not sub_is_active and self.is_ducking and not pygame.mixer.music.get_busy():
                self.vlc.set_volume(config.VOLUME_NORMAL)
                self.is_ducking = False

if __name__ == "__main__":
    app = DubbingDaemon()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nĐã tắt Trợ lý AI.")
