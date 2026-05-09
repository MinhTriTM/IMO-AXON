# Q[6] Khởi tạo dự án TMF Local Engine

## Câu hỏi
tự viết 1 engin đc ko. tạo thư mục dự án cho engin thử xem có đc không.

## Suy nghĩ (Thinking)
Người dùng muốn tự xây dựng engine. Tôi đã tư vấn về Piper TTS (VITS) vì đây là giải pháp thực tế nhất để có tốc độ < 300ms mà không cần card đồ họa quá khủng.
Tôi sẽ tạo thư mục `TMF_Local_Engine` nằm song song với `VLC_AI_Dubber`.

**Cấu trúc thư mục:**
- `models/`: Nơi chứa các file AI Model (.onnx, .json).
- `output/`: Nơi lưu file wav tạm thời.
- `scripts/`: Chứa các script cài đặt môi trường.
- `engine.py`: Lớp wrapper để gọi engine Piper từ Python.

**Lộ trình thực hiện cho người dùng:**
1. Cài đặt Piper (qua pip hoặc binary).
2. Tải model Tiếng Việt (vivos hoặc các bản nâng cao trên HuggingFace).
3. Tích hợp `TMFLocalEngine` vào `DubbingDaemon`.

## Câu trả lời
(Đã tạo thư mục và các file nền tảng)
