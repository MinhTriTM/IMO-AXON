# Q[3] Áp dụng các giải pháp Tối ưu TTS Realtime

## Câu hỏi
áp dụng cả 3 có thể lựa chọn và bổ sung thêm các cách khác nữa, realtime và giọng hay tiếng việt càng tốt.

## Suy nghĩ (Thinking)
Người dùng muốn tích hợp cả 3 phương án và thêm các lựa chọn khác.
1. **Edge TTS:** Cần cài đặt `edge-tts` và tạo một class `EdgeVoiceEngine`. Giọng tiếng Việt (HoaiMy, NamMinh) rất tốt và nhanh vì dùng WebSocket.
2. **Google Cloud TTS Streaming (gRPC):** Thay vì `synthesize_speech`, dùng `streaming_synthesize`. Tuy nhiên, Google Cloud TTS API cho Python hiện tại *không* hỗ trợ `streaming_synthesize` trực tiếp theo kiểu trả về stream âm thanh cho *Text-to-Speech* (nó chủ yếu hỗ trợ Streaming cho *Speech-to-Text*). Đối với TTS, Google trả về toàn bộ payload âm thanh. Để "streaming", ta phải tự chia nhỏ câu dài ra (chunking) và gửi nhiều request song song.
   *   *Đính chính kiến thức:* Gần đây Google có ra mắt streaming API hạn chế, nhưng cách tốt nhất để "realtime" với Google API hiện tại là **Sentence/Phrase Chunking** (chia nhỏ câu) kết hợp với **Smart Pre-fetching**.
3. **Smart Pre-fetching (Thuật toán tải trước thông minh):**
   *   Thay vì `pre_generate_all` từ đầu đến cuối (O(n)), ta sẽ lấy thời gian hiện tại của VLC, tìm index của câu sub tương ứng (O(log n) bằng binary search).
   *   Tạo một Queue/Worker Pool chỉ ưu tiên tải 5-10 câu *tiếp theo* tính từ vị trí hiện tại.
   *   Nếu người dùng tua phim, xóa hàng đợi cũ, bắt đầu tải lại từ vị trí mới.
4. **Bổ sung thêm:**
   *   **FPT AI TTS:** Giọng rất hay, có API miễn phí giới hạn ký tự. (Có thể làm module ẩn).
   *   **Zalo AI:** Giọng tốt, có API.
   *   *Quyết định:* Tập trung vào Edge TTS (Free, Realtime) và Google TTS (Chunking + Smart Prefetch) trước để hệ thống hoạt động ổn định.

**Kế hoạch triển khai:**
1. Cập nhật `config.py` để hỗ trợ chọn Engine (GOOGLE, EDGE).
2. Viết `EdgeVoiceEngine` sử dụng thư viện `edge-tts`.
3. Cải tiến `VoiceEngine` (Google) để chia nhỏ câu dài.
4. Cải tiến `DubbingDaemon` và thuật toán Prefetching:
   - Thêm bộ đệm (Queue) tải ưu tiên dựa trên thời gian VLC.
   - Xử lý sự kiện tua phim (seek) để hủy các tác vụ tải cũ không cần thiết.

## Câu trả lời
(Đang tiến hành implement và cập nhật code)
