import os
import sys

def welcome_mimo_axon():
    print("======================================================")
    print("   🚀 MIMO-AXON: Acoustic & X-media Orchestration")
    print("======================================================")
    print("\nChào mừng bạn đến với hệ sinh thái AI đa tác nhân.")
    print("Dự án được cấu trúc theo mô hình Modular Chuẩn Senior.")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    print("\n--- [DANH SÁCH MODULE SẴN SÀNG] ---")
    print(f"1. OCR Engine:     {os.path.join('src', 'core', 'ocr_engine.py')}")
    print(f"2. Dubbing Module: {os.path.join('src', 'modules', 'dubbing', 'TMF.py')}")
    print(f"3. TTS Module:     {os.path.join('src', 'modules', 'tts', 'fix_markdown.py')}")
    
    print("\n--- [HƯỚNG DẪN DỮ LIỆU] ---")
    print(f"Đầu vào (Video/Sub): {os.path.join('data', 'input')}")
    print(f"Đầu ra (Kết quả):    {os.path.join('data', 'output')}")
    
    print("\n--- [HƯỚNG DẪN CÀI ĐẶT] ---")
    print("1. Cài đặt thư viện: pip install -r requirements.txt")
    print("2. Cấu hình API Key: Copy .env.example thành .env và điền Key.")
    
    print("\n--- [KIỂM TRA HỆ THỐNG] ---")
    input_dir = os.path.join(BASE_DIR, "data", "input")
    if not os.path.exists(input_dir):
        os.makedirs(input_dir, exist_ok=True)
        print(f"✅ Đã khởi tạo thư mục dữ liệu: {input_dir}")
    else:
        print(f"✅ Thư mục dữ liệu đã sẵn sàng.")

    print("\n======================================================")
    print("   Project by: Đoàn Minh Trí - DTHU University")
    print("======================================================")

if __name__ == "__main__":
    welcome_mimo_axon()
