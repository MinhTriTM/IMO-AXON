# 📐 MIMO-AXON: Đặc tả Kỹ thuật Chi tiết (Technical Specifications)

Tài liệu này định nghĩa các tiêu chuẩn định lượng và yêu cầu kỹ thuật cho từng thành phần trong hệ sinh thái **MIMO-AXON**.

---

## 1. Module 1: Perception - Vision (OCR Engine)
Đặc tả quy trình trích xuất văn bản từ hình ảnh video.

| Thông số | Yêu cầu Kỹ thuật | Ghi chú |
| :--- | :--- | :--- |
| **Input Resolution** | Tối thiểu 720p (1280x720) | Đảm bảo độ sắc nét của ký tự |
| **Sampling Rate** | 1 frame/sec (Adaptive) | Tự động tăng lên 5 fps khi cảnh chuyển động nhanh |
| **OCR Model** | Gemini 2.5 Flash Lite | Tối ưu hóa cho Scene Text Detection |
| **Confidence Threshold** | > 85% | Bỏ qua các kết quả nhận diện không rõ ràng |
| **Crop Coordinates** | Bottom 20% (Default) | Có thể điều chỉnh qua config cho các loại video khác |

---

## 2. Module 2: Perception - Acoustic (STT Engine)
Đặc tả quy trình xử lý âm thanh và chuyển đổi giọng nói.

| Thông số | Yêu cầu Kỹ thuật | Ghi chú |
| :--- | :--- | :--- |
| **Audio Bitrate** | Tối thiểu 128 kbps | Đảm bảo dải tần số cho Whisper |
| **Sampling Frequency** | 16,000 Hz | Chuẩn đầu vào cho các mô hình STT hiện đại |
| **STT Model** | Whisper-large-v3 | Sử dụng bản phân giải cao nhất để đảm bảo dấu câu |
| **Diarization Error Rate** | < 10% | Độ chính xác khi phân biệt các người nói khác nhau |
| **Max Chunk Latency** | < 2000 ms | Thời gian tối đa để xử lý một đoạn thoại 5s |

---

## 3. Module 3: Cognitive - Translation (LLM Logic)
Đặc tả quy trình dịch thuật ngữ cảnh và suy luận chuỗi suy nghĩ (CoT).

| Thông số | Yêu cầu Kỹ thuật | Ghi chú |
| :--- | :--- | :--- |
| **Translation Engine** | Gemini 1.5 Pro | Hỗ trợ Context Window lên đến 2M tokens |
| **Reasoning Style** | Chain-of-Thought (CoT) | Phân tích bối cảnh trước khi đưa ra bản dịch |
| **Accuracy (BLEU/METEOR)** | > 0.85 | So soát với các bản dịch chuyên gia |
| **Terminology Consistency** | Bắt buộc (Glossary-based) | Giữ nguyên tên nhân vật và thuật ngữ xuyên suốt |
| **Length Constraints** | +/- 10% so với câu gốc | Đảm bảo không bị tràn thời lượng video |

---

## 4. Module 4: Action - Neural Dubbing (TTS Engine)
Đặc tả quy trình tổng hợp giọng nói và lồng tiếng.

| Thông số | Yêu cầu Kỹ thuật | Ghi chú |
| :--- | :--- | :--- |
| **Synthesis Engine** | Edge-TTS / Neural2 (Google) | Giọng nói tự nhiên, đa dạng cảm xúc |
| **Voice Variety** | > 20 Voices (Vi-VN) | Đủ cho các vai nam, nữ, già, trẻ |
| **Sync Accuracy** | +/- 50ms | Sai số tối đa giữa âm thanh thuyết minh và video |
| **Output Format** | MP3 / Opus (48kHz) | Chất lượng âm thanh phòng thu |
| **Dynamic Range** | -3dB to -6dB | Đảm bảo giọng đọc nổi bật trên nhạc nền |

---

## 5. Tiêu chuẩn Hệ thống chung (System KPIs)
- **Hệ số Hiệu suất:** 1 giờ video xử lý xong trong < 15 phút (tỷ lệ 4:1).
- **Độ tin cậy API:** 99.9% Uptime (Kết hợp cơ chế Retry & Fallback).
- **Tối ưu Token:** Sử dụng Cache để giảm 30% lượng token lặp lại.

---
**MIMO-AXON: Đặc tả chuẩn mực cho kỷ nguyên AI đa phương tiện.**
