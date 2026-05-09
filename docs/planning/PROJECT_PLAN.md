# Kế hoạch Chi tiết Dự án (Project Implementation Plan)

Dựa trên yêu cầu của bạn, dự án sẽ được triển khai theo 3 module cốt lõi (3 Cách) và tích hợp vào một hệ thống quản lý chung.

## Giai đoạn 1: Thiết lập nền tảng (Foundation)
- [ ] Khởi tạo môi trường Python/Node.js.
- [ ] Cấu hình FFmpeg trên Windows để xử lý video/audio.
- [ ] Thiết lập kết nối API (Gemini, Claude) để thực hiện dịch thuật và suy luận.

## Giai đoạn 2: Triển khai 3 Phương pháp xử lý

### Module 1: Xử lý qua Hình ảnh (OCR Sub)
- **Mục tiêu:** Trích xuất sub từ video không có file sub rời.
- **Kế hoạch:**
    1. Dùng FFmpeg cắt frame tại vùng chứa sub (crop).
    2. Gửi ảnh sang LLM Vision (Gemini 2.5 Flash Lite) để nhận dạng text (tối ưu tốc độ và chi phí).
    3. LLM tự động gộp text và gán timestamp tương đối.
    4. Dịch và xuất file `.srt`.

### Module 2: Xử lý qua Âm thanh (STT Sub) - *Ưu tiên cao*
- **Mục tiêu:** Độ chính xác cao, xử lý nhanh.
- **Kế hoạch:**
    1. Tách audio từ video (FFmpeg).
    2. Dùng OpenAI Whisper (Local hoặc API) để transcribe sang văn bản có timestamp.
    3. LLM (Gemini) thực hiện dịch thuật ngữ cảnh (giữ nguyên định dạng SRT).
    4. Tối ưu hóa file sub để khớp với video gốc.

### Module 3: Thuyết minh & Lồng tiếng (TTS Dubbing)
- **Mục tiêu:** Tạo trải nghiệm rạp chiếu phim đa ngôn ngữ.
- **Kế hoạch:**
    1. Lấy text đã dịch từ Module 1 hoặc 2.
    2. Sử dụng `edge-tts` (miễn phí, giọng đọc hay) hoặc tự build engine trên Win.
    3. Mix file âm thanh mới với video gốc, giảm âm lượng nhạc nền (audio ducking) nếu cần.
    4. Output ra file video đa track âm thanh.

## Giai đoạn 3: Tích hợp và Trình phát
- [ ] Xây dựng script tự động load sub/audio vào VLC hoặc MPC-HC thông qua command line.
- [ ] Viết giao diện điều khiển đơn giản (CLI hoặc Web UI).

## Giai đoạn 4: Hoàn thiện hồ sơ Xiaomi 100T
- [ ] Tổng hợp nhật ký (logs) xử lý để làm bằng chứng vận hành AI.
- [ ] Quay video demo quy trình từ video gốc đến video đã có thuyết minh.

---
*Lịch trình dự kiến: 2-3 tuần hoàn thiện MVP (Minimum Viable Product).*
