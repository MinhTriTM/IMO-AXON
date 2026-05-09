# ==========================================
# CẤU HÌNH VLC
# ==========================================
VLC_HOST = "127.0.0.1"
VLC_PORT = "8080"
VLC_PASSWORD = "1234" # Mật khẩu bạn đã set trong VLC > Lua HTTP

# ==========================================
# CẤU HÌNH AI DUBBING (TTS ENGINE)
# ==========================================
# Chọn Engine: "EDGE" (Khuyên dùng, miễn phí, siêu nhanh), "GOOGLE" (Chất lượng phòng thu)
TTS_ENGINE = "EDGE"  

# 1. Cấu hình Google Cloud TTS
GOOGLE_VOICE = "vi-VN-Neural2-A"

# 2. Cấu hình Microsoft Edge TTS (Miễn phí) - GIỌNG THUYẾT MINH PHIM HAY NHẤT
EDGE_VOICE = "vi-VN-HoaiMyNeural"

# Thông số tinh chỉnh cho giọng Hoài My nghe tự nhiên nhất
EDGE_RATE = "-10%" 
EDGE_PITCH = "+5Hz"

# Tốc độ nói chung cho các engine khác
SPEAKING_RATE = 1.0 

# ==========================================
# CẤU HÌNH HỆ THỐNG
# ==========================================
CACHE_DIR = "audio_cache"
VOLUME_DUCKING = 70  # Âm lượng VLC khi AI nói (256 là 100%)
VOLUME_NORMAL = 256  # Âm lượng VLC bình thường
PREFETCH_COUNT = 10  # Số câu thoại tải trước để đảm bảo Realtime
