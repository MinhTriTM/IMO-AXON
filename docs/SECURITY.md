# 🛡️ Chính sách Bảo mật (Security Policy)

Hệ thống **MIMO-AXON** coi trọng tính an toàn của dữ liệu và các tài sản trí tuệ của người dùng.

## 1. Bảo vệ API Keys
-   **Tuyệt đối không** push file `.env` lên GitHub.
-   Luôn sử dụng file `.env.example` làm mẫu để hướng dẫn cấu hình.
-   Các Agent của hệ thống được lập trình để không bao giờ in (log) các khóa bí mật ra màn hình console hoặc file log.

## 2. Xử lý Dữ liệu Đa phương tiện
-   Tất cả các file video/audio đầu vào trong thư mục `data/input/` đều được xử lý cục bộ trên máy của bạn.
-   Dữ liệu chỉ được gửi lên máy chủ AI (Gemini/Google Cloud) dưới dạng mã hóa qua giao thức HTTPS và sẽ không được lưu trữ vĩnh viễn trên các máy chủ này theo chính sách của Google API.

## 3. Báo cáo lỗ hổng bảo mật
Nếu bạn phát hiện bất kỳ vấn đề bảo mật nào, vui lòng **không** công khai trên GitHub Issues. Hãy gửi email trực tiếp cho chúng tôi tại: **minhtri132nhu016@gmail.com**. Chúng tôi sẽ phản hồi và xử lý trong vòng 48 giờ.

---
*MIMO-AXON: An toàn là nền tảng của sự thông minh.*
