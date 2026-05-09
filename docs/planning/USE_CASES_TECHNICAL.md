# 🧠 MIMO-AXON: Đặc tả Use Cases Kỹ thuật Chuyên sâu (Senior Level)

Tài liệu này trình bày các kịch bản sử dụng phức tạp nhất, minh chứng cho khả năng điều phối đa tác nhân (Multi-Agent) và giải quyết các bài toán kỹ thuật biên (Edge Cases).

---

## Use Case 1: Trích xuất & Dịch thuật Phụ đề đa lớp (Multi-layer Hard-sub Processing)
**Bối cảnh:** Video có nhiều lớp văn bản (sub gốc, text quảng cáo, watermark) đè lên nhau hoặc sub xuất hiện tại nhiều vị trí khác nhau trên màn hình.

### 1.1 Luồng thực thi đa tác nhân:
1.  **Agent Visual Scout (Gemini 2.5 Flash Lite):** 
    -   Thực hiện "Dynamic Spatial Sampling": Không chỉ quét vùng dưới, AI tự động nhận diện toàn bộ khung hình để tìm kiếm các vùng chứa ký tự (Scene Text Detection).
    -   Trích xuất metadata về tọa độ (x, y, w, h) của từng khối text.
2.  **Logic Layer (Python/FFmpeg):** 
    -   Áp dụng "Differential Pixel Analysis": So sánh sự thay đổi của các pixel trong vùng tọa độ qua nhiều frame để phân biệt giữa Text tĩnh (Watermark) và Text động (Subtitle).
3.  **Agent Contextual Translator (Gemini 1.5 Pro):** 
    -   Nhận diện ngữ cảnh từ hình ảnh xung quanh text để quyết định đâu là nội dung cần dịch chính yếu, loại bỏ các text "nhiễu" (quảng cáo).

### 1.2 Giải quyết lỗi biên (Edge Cases):
-   **Text trùng màu nền:** Sử dụng FFmpeg filters `negate` hoặc `threshold` để làm nổi bật cạnh chữ trước khi gửi sang AI.
-   **Chữ chạy (Scrolling Text):** Thuật toán gộp chuỗi ký tự dựa trên sự dịch chuyển tọa độ vector.

---

## Use Case 2: Lồng tiếng Đa nhân vật & Phân tích Cảm xúc (Emotional Multi-Speaker Dubbing)
**Bối cảnh:** Một bộ phim Anime có 5 nhân vật với các giới tính và độ tuổi khác nhau, kèm theo các phân đoạn cao trào (khóc, cười, tức giận).

### 2.1 Luồng thực thi đa tác nhân:
1.  **Agent Acoustic Analyst (Whisper-v3 + Pyannote):** 
    -   "Speaker Diarization": Phân tách audio thành các track riêng biệt cho từng người nói (Speaker A, B, C...).
    -   Gán nhãn giới tính và ước lượng độ tuổi dựa trên phổ tần số âm thanh.
2.  **Agent Semantic Emotion (Claude 3.5 Sonnet / Gemini Pro):**
    -   Phân tích văn bản đã dịch để xác định "Sentiment Profile" cho từng câu thoại.
    -   Đưa ra chỉ thị TTS cụ thể: `{voice: "HoaiMy", style: "Angry", speed: "1.2x", pitch: "+5Hz"}`.
3.  **Agent Neural Dubber (Edge-TTS / Local Engine):**
    -   Tạo audio track cho từng nhân vật với các Voice ID khác nhau.
    -   "Duration Matching": Tự động cắt/nối khoảng lặng hoặc điều chỉnh tốc độ nói (time-stretching) để khớp 100% với khẩu hình nhân vật.

---

## Use Case 3: Hệ thống Dịch thuật & Thuyết minh Song song (Real-time Live Overlay)
**Bối cảnh:** Người dùng xem một buổi Live Stream trực tiếp trên YouTube/Twitch và muốn có thuyết minh tiếng Việt ngay lập tức.

### 3.1 Luồng thực thi đa tác nhân:
1.  **Stream Buffer Engine:** 
    -   Bắt gói tin (Capture stream) theo từng đoạn ngắn 5 giây (Chunk-based processing).
2.  **Agent Parallel Pipeline:**
    -   **Task A:** Whisper trích xuất text từ chunk hiện tại.
    -   **Task B:** Gemini Flash dịch thuật siêu tốc (< 1s latency).
    -   **Task C:** Edge-TTS tạo audio và đẩy vào kênh âm thanh ảo (Virtual Audio Cable).
3.  **Synchronization Logic:** 
    -   Sử dụng "Elastic Buffering" để giữ cho độ trễ âm thanh thuyết minh không lệch quá 3 giây so với hình ảnh trực tiếp.

---

## Use Case 4: Chế bản Nội dung Tự động Toàn cầu (Global Content Distribution)
**Bối cảnh:** Tự động hóa việc biến 1 video gốc thành 10 phiên bản ngôn ngữ khác nhau để đăng tải lên YouTube Global.

### 4.1 Quy trình vận hành công nghiệp:
1.  **Batch Processing:** Hệ thống quét thư mục `data/input`, tự động xếp hàng (Queue) hàng trăm video.
2.  **MIMO-AXON Orchestration:** 
    -   Tự động tách nhạc nền (BGM) và giọng nói (Vocal).
    -   Dịch thuật đa ngôn ngữ song song.
    -   Lồng tiếng hàng loạt với 10 ngôn ngữ mục tiêu.
3.  **Final Assembly (FFmpeg):** 
    -   Ghép 10 bản audio thuyết minh vào 10 file video output riêng biệt.
    -   Tự động tạo Thumbnail và Tiêu đề video bằng AI dựa trên nội dung đã dịch.

---

## Use Case 5: Tách nguồn âm thanh & Lồng tiếng sạch (Vocal Isolation & Background Preservation)
**Bối cảnh:** Video gốc có nhạc nền (BGM) và hiệu ứng âm thanh (SFX) đan xen với giọng nói. Việc lồng tiếng mới không được làm mất đi các âm thanh môi trường này.

### 5.1 Luồng thực thi:
1.  **Agent Acoustic Separator (Spleeter/Demucs Engine):**
    -   Sử dụng mô hình tách nguồn (Source Separation) để chia file audio thành 2 track: `vocal.wav` và `background.wav`.
2.  **Logic Layer:**
    -   `vocal.wav` được gửi sang Whisper để STT.
    -   `background.wav` được giữ nguyên làm lớp nền (Ambient track).
3.  **Final Mixing:**
    -   Trộn audio thuyết minh mới vào `background.wav` sử dụng kỹ thuật **Audio Ducking** (tự động giảm âm lượng nhạc nền khi có tiếng nói).

---

## Use Case 6: Đồng bộ hóa nhịp điệu & Khẩu hình (Lip-Sync Rhythm Alignment)
**Bối cảnh:** Câu dịch có độ dài âm tiết khác biệt hoàn toàn so với câu gốc, gây hiện tượng lệch khẩu hình (lip-sync mismatch).

### 6.1 Luồng thực thi:
1.  **Duration Analysis:** AI đo chính xác độ dài (ms) của đoạn thoại gốc.
2.  **Adaptive TTS Generation:** 
    -   Nếu câu dịch dài hơn: Tự động tăng `rate` (tốc độ) và điều chỉnh `pitch` để không bị méo tiếng.
    -   Nếu câu dịch ngắn hơn: Tự động chèn thêm các khoảng lặng thông minh (smart silence) vào giữa các cụm từ dựa trên dấu câu.
3.  **Post-processing:** Sử dụng FFmpeg `atempo` filter để tinh chỉnh độ dài âm thanh cuối cùng mà không làm thay đổi cao độ giọng đọc.

---

## Use Case 7: Tăng cường chất lượng âm thanh nhiễu (Speech Enhancement in Noisy Streams)
**Bối cảnh:** Nguồn đầu vào là video quay ngoài trời, hội thảo có nhiều tiếng ồn trắng, tiếng gió hoặc nhiễu kỹ thuật.

### 7.1 Luồng thực thi:
1.  **Denoising Agent:** Sử dụng mô hình Deep Learning (như RNNoise hoặc Facebook Denoiser) để lọc nhiễu môi trường trước khi thực hiện STT.
2.  **Semantic Reconstruction:** 
    -   Nếu một đoạn thoại bị mất do nhiễu nặng, Agent Contextual sẽ dựa vào các câu trước và sau để "suy luận" và bù đắp nội dung còn thiếu (Inpainting text).
3.  **Verification:** Đối soát nội dung suy luận với các tín hiệu âm thanh còn sót lại để đảm bảo tính xác thực.

---
**MIMO-AXON: Kiến trúc của sự tối ưu và hiệu suất vượt giới hạn.**
