import re
import os

def normalize_markdown(input_file):
    """
    Chuẩn hóa định dạng Markdown.
    Hỗ trợ đường dẫn tương đối (Portable).
    """
    if not os.path.exists(input_file):
        print(f"❌ Không tìm thấy file tại: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    template = """## TỔNG QUAN\nBối cảnh: [Thông tin]\nLogic: [Đa tác nhân]\n"""
    pattern = r'\*\*\*(\d{4}):\*\*\*(.*?)(?=\*\*\*\d{4}:\*\*\*|\Z)'

    def normalize_year(match):
        year = match.group(1)
        return f"## {year}\n\n{template}\n\n---\n\n"

    new_content = re.sub(pattern, normalize_year, content, flags=re.DOTALL)
    
    if not new_content.startswith("# "):
        new_content = "# Môn Lịch Sử Đảng Theo Dòng Thời Gian\n\n---\n\n" + new_content

    with open(input_file, 'w', encoding='utf-8-sig') as f:
        f.write(new_content)

    print(f"✅ Đã chuẩn hóa thành công: {input_file}")

if __name__ == "__main__":
    # Cấu hình đường dẫn mềm trỏ vào docs/research
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
    target_path = os.path.join(BASE_DIR, "docs", "research", "timeline.md")
    
    normalize_markdown(target_path)
