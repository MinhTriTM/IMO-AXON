# Q[2] Tối ưu hóa Google TTS cho Realtime

## Câu hỏi
tốc độ google api trả về khá lâu nên ko dùng realtime được phải làm sao. tôi muốn nó như app T2S trên android, dùng engin TTS google realtime, dù có chọn giọng network nhưng nó vẫn realtime.

## Suy nghĩ (Thinking)
Người dùng đang gặp vấn đề về độ trễ (latency) của Google Cloud TTS API. Trong khi đó, các ứng dụng như T2S trên Android dường như hoạt động mượt mà hơn.
Nguyên nhân có thể là do:
1. **Mạng (Network):** Cloud API yêu cầu gửi request lên server và nhận file về.
2. **Cơ chế xử lý:** Hiện tại code đang gọi API cho từng dòng sub khi đến giờ chơi (dù có `pre_generate_all` nhưng có vẻ vẫn bị nghẽn hoặc chưa tối ưu).
3. **Engine khác nhau:** T2S trên Android dùng Android TTS Engine (có thể gọi trực tiếp Google TTS app trên máy - gRPC hoặc Local Engine nếu đã tải gói ngôn ngữ).

Giải pháp đề xuất:
- **Streaming (gRPC):** Google Cloud hỗ trợ streaming âm thanh, giúp phát ngay khi những byte đầu tiên được trả về.
- **Edge TTS (Microsoft):** Một lựa chọn thay thế rất nhanh và miễn phí (không cần API key chính thức) thường được dùng trong các tool lồng tiếng nhanh.
- **Pre-fetching thông minh:** Cải thiện `pre_generate_all` để không chỉ chạy ngầm mà còn ưu tiên các câu sắp đến.
- **Dùng Google TTS qua thư viện khác:** Ví dụ `gTTS` (dùng API dịch thuật, chậm hơn nhưng đơn giản) hoặc các wrapper tối ưu.

## Câu trả lời
(Sẽ được cập nhật sau khi phân tích kỹ hơn và thảo luận với người dùng)
