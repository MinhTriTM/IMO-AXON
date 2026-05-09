from google.cloud import texttospeech

# Khởi tạo client - nó sẽ tự dùng quyền từ gcloud login của bạn
client = texttospeech.TextToSpeechClient()

# Nội dung muốn đọc
input_text = texttospeech.SynthesisInput(text="Chào bạn, mình là giọng nữ miền Bắc rất tự nhiên của Google.")

# Cấu hình giọng nói (Neural2-A là giọng nữ Bắc cực hay)
voice = texttospeech.VoiceSelectionParams(
    language_code="vi-VN",
    name="vi-VN-Neural2-A" 
)

# Cấu hình file đầu ra (MP3)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1.05  # Tăng một chút tốc độ nghe sẽ tự nhiên hơn
)

# Gọi API
response = client.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
)

# Lưu file
with open("test_giong_nu.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Xong rồi! Bạn mở file test_giong_nu.mp3 lên nghe thử nhé.")
