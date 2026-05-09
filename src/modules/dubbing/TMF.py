import asyncio
import pysubs2
import re
import time
import pygame
import edge_tts
import io
import os

# --- CẤU HÌNH ĐƯỜNG DẪN MỀM ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
INPUT_DIR = os.path.join(BASE_DIR, "data", "input")

# Tự động tìm file .ass trong data/input
if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR, exist_ok=True)

ass_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.ass')]
if not ass_files:
    print(f"⚠️ Cảnh báo: Không thấy file .ass nào trong {INPUT_DIR}")
    SUB_FILE = os.path.join(INPUT_DIR, "sample.ass")
else:
    SUB_FILE = os.path.join(INPUT_DIR, ass_files[0])

VOICE = "vi-VN-HoaiMyNeural" 
PRE_READ_MS = 1800 

def clean_text(text):
    text = re.sub(r'\{.*?\}', '', text)
    return text.replace(r'\N', ' ').replace(r'\n', ' ').strip()

RATE = "+20%"
PITCH = "+6Hz"
VOLUME = "+0%"

async def play_tts(text):
    try:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH, volume=VOLUME)
        data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                data += chunk["data"]
        
        audio_file = io.BytesIO(data)
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"\nLỗi phát âm thanh: {e}")

async def main():
    print(f"--- Đang nạp hệ thống thuyết minh: {SUB_FILE} ---")
    if not os.path.exists(SUB_FILE):
        print(f"❌ Lỗi: Vui lòng đặt file phụ đề vào {INPUT_DIR}")
        return
    
    subs = pysubs2.load(SUB_FILE, encoding="utf-8")
    subs.sort() 
    
    pygame.mixer.init()
    print(f"\n[SẴN SÀNG] Mở phim ở giây 00:00")
    input("Nhấn ENTER rồi bấm PLAY trên VLC...")
    
    start_time = time.time() * 1000 
    for line in subs:
        text_to_read = clean_text(line.text)
        if not text_to_read or len(text_to_read) < 2: continue
        trigger_time = line.start - PRE_READ_MS
        
        while True:
            elapsed = (time.time() * 1000) - start_time
            if elapsed >= trigger_time:
                print(f"\n[ĐANG ĐỌC] {text_to_read}")
                await play_tts(text_to_read)
                break
            await asyncio.sleep(0.01)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nĐã dừng.")
