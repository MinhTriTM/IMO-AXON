# Truy vấn Q6: Triển khai OCR Subtitle Extraction với Gemini 2.5 Flash Lite

**Câu hỏi của người dùng:**
OCR Subtitle Extraction dùng gemini-2.5-flash_lite

**Suy nghĩ của Agent:**
- Người dùng chỉ định sử dụng mô hình `gemini-2.5-flash-lite` cho tác vụ OCR. Đây là lựa chọn tối ưu vì Flash Lite có tốc độ xử lý ảnh nhanh và chi phí token thấp, phù hợp cho việc xử lý hàng loạt frames video.
- Tôi đã cập nhật mô hình này vào các tài liệu chiến lược (`DASHBOARD.html`, `PROJECT_PLAN.md`).
- Tôi đã viết một script Python mẫu (`ocr_module_v1.py`) tích hợp lệnh FFmpeg để cắt vùng chứa sub (crop 20% dưới cùng) nhằm tối ưu hóa đầu vào cho Gemini Vision.

**Câu trả lời:**
Đã thiết lập Module OCR sử dụng **Gemini 2.5 Flash Lite**. Hệ thống sẽ trích xuất frames từ video thông qua FFmpeg và sử dụng khả năng Vision của Flash Lite để nhận diện văn bản phụ đề một cách hiệu quả nhất.
