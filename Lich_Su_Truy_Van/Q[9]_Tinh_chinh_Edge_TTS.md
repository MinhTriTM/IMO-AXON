# Q[9] Tinh chỉnh thông số Edge TTS (Rate & Pitch)

## Câu hỏi
Sử dụng cấu hình: `communicate = edge_tts.Communicate(text, "vi-VN-HoaiMyNeural", rate="-10%", pitch="+5Hz")`

## Suy nghĩ (Thinking)
Người dùng đã tìm ra thông số "vàng" để giọng Hoài My nghe hay nhất:
- `rate="-10%"`: Đọc chậm lại một chút để rõ chữ và có chiều sâu hơn.
- `pitch="+5Hz"`: Tăng nhẹ cao độ giúp giọng nữ nghe trẻ trung và thanh thoát hơn.

Tôi sẽ áp dụng cấu hình này vào:
1. `VLC_AI_Dubber\config.py`: Để lưu trữ biến cấu hình toàn cục.
2. `VLC_AI_Dubber\main.py`: Để áp dụng vào logic thuyết minh chính.
3. `TMF_Local_Engine\selector_tts.py`: Để cập nhật công cụ test bảng chọn.

## Câu trả lời
(Đã cập nhật tất cả các file liên quan với thông số mới)
