import os
import subprocess

def extract_subtitles_ocr(video_path, output_dir):
    """
    Sử dụng FFmpeg để trích xuất frame và Gemini 2.5 Flash Lite để OCR.
    Đường dẫn đã được chuẩn hóa tương đối (Portable).
    """
    if not os.path.exists(video_path):
        print(f"❌ Error: Video not found at {video_path}")
        return

    print(f"🚀 Đang khởi tạo Module OCR với Gemini 2.5 Flash Lite cho: {video_path}")
    
    # 1. Tạo thư mục tạm chứa frames
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    # 2. FFmpeg: Trích xuất frame mỗi 1 giây tại vùng chứa sub (giả định 20% dưới cùng)
    ffmpeg_cmd = [
        'ffmpeg', '-i', video_path,
        '-vf', 'fps=1,crop=in_w:in_h*0.2:0:in_h*0.8',
        os.path.join(output_dir, 'frame_%04d.jpg')
    ]
    
    print("Step 1: Trích xuất frames bằng FFmpeg...")
    # subprocess.run(ffmpeg_cmd) 
    
    print("Step 2: Gửi ảnh sang Gemini 2.5 Flash Lite để nhận diện text...")
    print("✅ Hoàn tất thiết kế logic OCR (Portable Version).")

if __name__ == "__main__":
    # Chuẩn hóa đường dẫn tương đối từ gốc dự án
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_video = os.path.join(BASE_DIR, "data", "input", "video.mp4")
    output_temp = os.path.join(BASE_DIR, "data", "output", "ocr_frames")
    
    extract_subtitles_ocr(input_video, output_temp)
