
import os
import re
import pysubs2
from google.cloud import texttospeech
from tqdm import tqdm

# --- CẤU HÌNH ---
# Tự động tìm file .ass trong thư mục
try:
    SUB_FILE = next(f for f in os.listdir('.') if f.endswith('.ass'))
    print(f"Đã tìm thấy file phụ đề: {SUB_FILE}")
except StopIteration:
    print("LỖI: Không tìm thấy file .ass nào trong thư mục hiện tại.")
    exit()

# Thư mục để lưu trữ các file audio đã được tạo
AUDIO_CACHE_DIR = "audio_cache"

# Cấu hình giọng nói của Google Cloud TTS
# Bạn có thể thay đổi các giá trị này theo file ý tưởng.txt
# Giọng Neural2 (chất lượng cao, giá hợp lý)
# vi-VN-Neural2-A (Nữ - Bắc)
# vi-VN-Neural2-B (Nam - Bắc)
# vi-VN-Neural2-D (Nữ - Nam)
# Giọng Studio (chất lượng cao nhất, đắt hơn)
# vi-VN-Studio-C (Nữ)
VOICE_NAME = "vi-VN-Neural2-A"
SPEAKING_RATE = 1.05 # Tốc độ nói (1.0 là bình thường)

# --- CÁC HÀM TIỆN ÍCH ---

def clean_text(text):
    """
    Dọn dẹp text từ file .ass, xóa các tag định dạng.
    Ví dụ: {\an8}Chào bạn -> Chào bạn
    """
    # Xóa các tag kiểu {...}
    text = re.sub(r'{.+?}', '', text)
    # Thay thế ký tự xuống dòng của sub bằng khoảng trắng
    return text.replace('\N', ' ').replace('
', ' ').strip()

def pre_generate_audio():
    """
    Hàm chính để đọc file sub, gọi API và lưu file audio.
    """
    print("--- BẮT ĐẦU QUÁ TRÌNH TẠO KHO ÂM THANH ---")

    # 1. Khởi tạo client của Google
    # Lệnh này sẽ tự động sử dụng quyền bạn đã cấp qua "gcloud auth application-default login"
    try:
        client = texttospeech.TextToSpeechClient()
        print("Đã khởi tạo Google TextToSpeechClient thành công.")
    except Exception as e:
        print(f"LỖI: Không thể khởi tạo Google TTS Client. Bạn đã cài đặt Google Cloud SDK và đăng nhập chưa?")
        print(f"Lỗi chi tiết: {e}")
        return

    # 2. Tạo thư mục cache nếu chưa có
    if not os.path.exists(AUDIO_CACHE_DIR):
        os.makedirs(AUDIO_CACHE_DIR)
        print(f"Đã tạo thư mục cache: {AUDIO_CACHE_DIR}")

    # 3. Đọc và sắp xếp file phụ đề
    # Dùng utf-8-sig để xử lý các file có BOM (Byte Order Mark)
    try:
        subs = pysubs2.load(SUB_FILE, encoding="utf-8-sig")
        subs.sort() # Đảm bảo các dòng sub được sắp xếp theo đúng thứ tự thời gian
        print(f"Đã đọc và sắp xếp {len(subs)} dòng phụ đề từ {SUB_FILE}.")
    except Exception as e:
        print(f"LỖI: Không thể đọc file phụ đề {SUB_FILE}.")
        print(f"Lỗi chi tiết: {e}")
        return

    # 4. Cấu hình giọng nói và audio
    voice_params = texttospeech.VoiceSelectionParams(
        language_code="vi-VN",
        name=VOICE_NAME
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=SPEAKING_RATE
    )

    # 5. Vòng lặp qua từng dòng sub để tạo audio
    print("
Bắt đầu tạo file audio cho từng dòng sub:")
    # tqdm là thư viện giúp tạo thanh tiến trình đẹp mắt
    for i, line in enumerate(tqdm(subs, desc="Đang xử lý sub")):
        output_filename = os.path.join(AUDIO_CACHE_DIR, f"{i}.mp3")

        # KIỂM TRA ĐỂ TIẾT KIỆM CHI PHÍ: Nếu file đã tồn tại, bỏ qua
        if os.path.exists(output_filename):
            continue

        text_to_read = clean_text(line.text)

        # Bỏ qua các dòng trống hoặc quá ngắn
        if not text_to_read or len(text_to_read) < 2:
            continue

        try:
            synthesis_input = texttospeech.SynthesisInput(text=text_to_read)

            # Gọi API
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice_params,
                audio_config=audio_config
            )

            # Lưu file audio
            with open(output_filename, "wb") as out:
                out.write(response.audio_content)

        except Exception as e:
            print(f"
LỖI khi xử lý dòng {i}: {text_to_read}")
            print(f"Lỗi chi tiết: {e}")
            # Nếu có lỗi, tạo một file trống để không xử lý lại dòng này
            with open(output_filename, "w") as f:
                f.write('')


    print("
--- HOÀN TẤT! ---")
    print(f"Toàn bộ audio thuyết minh đã được tạo và lưu trong thư mục '{AUDIO_CACHE_DIR}'.")

# --- ĐIỂM BẮT ĐẦU CỦA SCRIPT ---
if __name__ == "__main__":
    pre_generate_audio()
