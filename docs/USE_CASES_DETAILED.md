# Tài liệu Use Cases Chi tiết - Dự án OmniTrans AI

Tài liệu này mô tả các kịch bản vận hành hệ thống dưới góc độ kiến trúc phần mềm chuyên sâu (Senior Level), tập trung vào tính logic, khả năng xử lý lỗi và tối ưu hóa hiệu suất AI.

---

## Use Case 1: Tái cấu trúc Phụ đề từ Video (Hard-coded Sub Recovery)
**Mục tiêu:** Trích xuất và dịch phụ đề từ các video đã bị "burn-in" sub (không có file rời), đảm bảo độ khớp thời gian chính xác.

### 1.1 Luồng Logic chính (Main Flow)
1. **Phân tích Frame thông minh:** Thay vì trích xuất toàn bộ video (gây tốn kém), Agent sử dụng FFmpeg để chụp ảnh mỗi 0.5s - 1s tại vùng tọa độ xác định (thường là 20% dưới cùng của khung hình).
2. **Vision-Language Orchestration:** 
   - **Step A:** Gửi Batch Frames sang Gemini 1.5 Flash (tối ưu chi phí).
   - **Step B:** AI nhận diện text và trả về định dạng JSON: `{timestamp: "00:12", text: "..."}`.
3. **LLM Contextual Refinement:** Một Agent khác (Gemini 1.5 Pro hoặc Claude) nhận dữ liệu thô để sửa lỗi chính tả do OCR và gộp các câu bị ngắt quãng giữa các frame.
4. **Translation Pipeline:** Dịch thuật dựa trên ngữ cảnh toàn bộ đoạn video thay vì dịch từng dòng (để giữ được sắc thái nhân vật).

### 1.2 Xử lý lỗi & Biên (Edge Cases - Senior Insights)
- **Sub bị che khuất bởi watermark:** Sử dụng thuật toán so sánh Pixel giữa các frame để loại bỏ các vùng text tĩnh (watermark) và chỉ lấy text thay đổi (sub).
- **Sub chạy quá nhanh:** Thuật toán tự động điều chỉnh khoảng thời gian chụp (sampling rate) linh hoạt khi phát hiện mật độ text thay đổi cao.

---

## Use Case 2: Hệ thống Lồng tiếng Đa ngôn ngữ (End-to-End AI Dubbing)
**Mục tiêu:** Chuyển đổi ngôn ngữ video gốc sang ngôn ngữ đích bao gồm cả âm thanh, giữ nguyên cảm xúc.

### 2.1 Luồng Logic chính (Main Flow)
1. **Source Separation (Vocal/BGM):** Sử dụng mô hình tách nguồn âm thanh (như Demucs/Spleeter) để tách riêng giọng nói (Vocal) và nhạc nền (BGM).
2. **STT & Alignment:** Whisper-large-v3 trích xuất văn bản gốc kèm timestamp cực chuẩn (word-level timestamps).
3. **Emotional Translation:** LLM nhận chỉ thị dịch thuật kèm theo "Tone of Voice" (ví dụ: hài hước, trang trọng).
4. **Speed-controlled TTS:** 
   - Tính toán độ dài chuỗi ký tự sau khi dịch.
   - Nếu câu dịch dài hơn câu gốc, Agent tự động gọi API TTS với tham số `pitch` và `rate` được điều chỉnh để khớp chính xác với thời lượng (Duration Matching) của clip gốc.
5. **Audio Multiplexing:** Trộn Vocal mới (đã thuyết minh) với BGM gốc bằng FFmpeg Audio Filters.

### 2.2 Senior Logic
- **Handle Silence:** Tự động phát hiện các khoảng lặng trong audio gốc để chèn Vocal mới vào đúng vị trí, tránh tình trạng "trôi sub" hoặc "trôi tiếng".
- **Speaker Diarization:** Nhận diện các giọng nói khác nhau (Nhân vật A, Nhân vật B) để gán các giọng TTS khác nhau, tạo sự sống động.

---

## Use Case 3: Tích hợp Trình phát Media (VLC/MPC Integration)
**Mục tiêu:** Tạo trải nghiệm người dùng liền mạch thông qua các ứng dụng sẵn có.

### 3.1 Luồng Logic chính (Main Flow)
1. **Watchdog Service:** Một script chạy ngầm theo dõi thư mục `Input_Video`.
2. **Auto-Processing:** Khi có video mới, hệ thống tự động kích hoạt Module 1 hoặc 2.
3. **IPC (Inter-Process Communication):** Sử dụng Command Line Arguments của VLC/MPC để mở video kèm theo file sub/audio vừa tạo:
   - `vlc.exe video.mp4 --sub-file=generated_sub.srt`
   - `mpc-hc.exe video.mp4 /dub audio_en.mp3`

### 3.2 Senior Logic
- **Lazy Loading:** Chỉ xử lý 5 phút đầu của video để người dùng xem ngay, trong khi đó hệ thống tiếp tục xử lý phần còn lại dưới background (Stream processing).
- **Cache Management:** Lưu trữ các đoạn đã dịch để tái sử dụng nếu người dùng mở lại cùng một video hoặc video có nội dung tương tự.

---
**Ghi chú kỹ thuật:** Hệ thống ưu tiên kiến trúc **Stateless** để dễ dàng triển khai lên Docker hoặc Cloud Functions sau này.
