# BẢN THUYẾT MINH DỰ ÁN: MIMO-AXON (Ứng tuyển Xiaomi MIMO 100T)

*Dành cho: Hội đồng đánh giá Xiaomi MIMO*
*Ứng viên: **Đoàn Minh Trí - DTHU University** (minhtri132nhu016@gmail.com)*

---

## 04. Mô tả cụ thể kết quả dự án (Project Description)

### 1. Vấn đề cốt lõi giải quyết:
Dự án mật danh **MIMO-AXON** giải quyết rào cản ngôn ngữ trong việc tiêu thụ nội dung đa phương tiện quy mô lớn. Hiện nay, quy trình dịch thuật, làm phụ đề và lồng tiếng (dubbing) thủ công tốn trung bình 5-10 giờ cho mỗi 1 giờ video. MIMO-AXON tự động hóa 95% quy trình này, giúp người dùng phổ cập kiến thức từ mọi ngôn ngữ sang tiếng địa phương với chi phí thấp và độ trễ tối thiểu.

### 2. Luồng logic cốt lõi (Multi-Agent & CoT):
Hệ thống vận hành dựa trên kiến trúc **Collaborative Multi-Agent System** phối hợp với **Chain-of-Thought (CoT) Reasoning**:

*   **Agent A (Visual Scout):** Sử dụng FFmpeg tích hợp Gemini 2.5 Flash Lite để quét các khung hình, nhận diện sự thay đổi của phụ đề cứng (hard-sub). CoT được áp dụng để Agent tự quyết định tần suất lấy mẫu (sampling rate) dựa trên tốc độ diễn biến của video.
*   **Agent B (Acoustic Analyst):** Sử dụng mô hình Whisper kết hợp với logic hậu xử lý để lọc nhiễu, tách Vocal/BGM và gán nhãn định danh người nói (Speaker Diarization).
*   **Agent C (Contextual Translator):** Đây là "bộ não" sử dụng Gemini 1.5 Pro. Thay vì dịch từng dòng, Agent này đọc toàn bộ văn bản thô để hiểu ngữ cảnh, văn hóa và chuyên môn, sau đó mới thực hiện dịch thuật CoT để đảm bảo tính tự nhiên và khớp thời lượng (Duration Matching).
*   **Agent D (Neural Orchestrator):** Điều phối các công cụ TTS (Edge-TTS/Local) để tạo giọng đọc lồng tiếng, tự động điều chỉnh cao độ và tốc độ để khớp hoàn hảo với chuyển động môi (Lip-sync alignment logic).

### 3. Kết quả dự đoán:
Dự kiến hệ thống có khả năng xử lý hàng nghìn giờ nội dung mỗi tháng, tiêu thụ khoảng 500M - 1.5B tokens tùy quy mô, cải thiện hiệu suất sản xuất nội dung lên **850%** so với quy trình thủ công.

---

## 05. Bằng chứng năng lực (Evidence of Impact)
*   **Kỹ thuật:** Sử dụng FFmpeg để xử lý stream video ngay trên thiết bị đầu cuối Windows, tích hợp API Gemini 2.5 cho tốc độ xử lý sub < 30s/clip.
*   **Mã nguồn:** Kiến trúc được module hóa cực cao, sẵn sàng triển khai trên các hệ thống phân tán (Distributed Systems).
*   **Trực quan:** Dashboard giám sát Real-time tích hợp HTML/Markdown giúp theo dõi chính xác lượng token tiêu thụ và trạng thái của từng Agent.
