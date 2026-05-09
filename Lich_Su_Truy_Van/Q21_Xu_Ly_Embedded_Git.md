# Truy vấn Q21: Xử lý lỗi Embedded Git Repositories (Repo lồng nhau)

**Câu hỏi của người dùng:**
Git báo cảnh báo "adding embedded git repository" khi thực hiện `git add .`.

**Suy nghĩ của Agent:**
- Nguyên nhân: Các thư mục như `MeloTTS-Vietnamese`, `XTTS-v2`, `espeak-ng` được clone từ nguồn khác và chứa sẵn thư mục `.git` của riêng chúng.
- Nếu không xử lý, Git chính của dự án MIMO-AXON sẽ chỉ lưu "link" đến các repo này mà không lưu code thực tế (lỗi submodule trống).
- Cách giải quyết chuẩn Senior: Xóa các thư mục `.git` ẩn bên trong các module con để Git chính nhận diện toàn bộ file là mã nguồn của dự án hiện tại.
- Sau đó cần làm sạch cache của Git để cập nhật lại cấu trúc đúng.

**Câu trả lời:**
Đây là vấn đề "Repo trong Repo". Để mã nguồn của MeloTTS, XTTS hay espeak-ng thực sự xuất hiện trên GitHub của bạn, chúng ta cần xóa bỏ các thư mục `.git` ẩn của chúng. Tôi đã soạn sẵn các lệnh PowerShell để bạn thực hiện việc này một cách an toàn và nhanh chóng.
