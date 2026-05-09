# Q8: Tổ chức lại cấu trúc thư mục Senior

📋 **Yêu cầu:** Tổ chức lại toàn bộ dự án XiaoMi100T theo cấu trúc thư mục hiện đại, tinh nhuệ.

🧠 **Suy nghĩ:**
- Dự án hiện đang để các file lộn xộn ở root và các thư mục module chưa đồng nhất.
- Cần chuyển docs vào `docs/`, code vào `src/`, dữ liệu vào `data/` và giao diện vào `web/`.
- Sử dụng lệnh `move` để xử lý các file lớn như `.mkv` trong `Thuyet_Minh_Film`.
- Sau khi di chuyển, cần kiểm tra và dọn dẹp thư mục cũ.

🔧 **Thao tác:**
1. Tạo các thư mục: `docs/proposal`, `docs/research`, `src/core`, `src/modules/stt`, `src/modules/tts`, `src/modules/dubbing`, `data/input`, `data/output`, `web`.
2. Di chuyển các file đơn lẻ ở root vào vị trí mới.
3. Di chuyển nội dung `T2S/` vào `src/modules/tts/`.
4. Di chuyển nội dung `Thuyet_Minh_Film/` vào `src/modules/dubbing/`.
5. Xóa thư mục cũ.

✅ **Kết quả:** Đang thực hiện...
