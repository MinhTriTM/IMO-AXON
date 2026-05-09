import asyncio
import edge_tts

async def list_voices():
    voices = await edge_tts.VoicesManager.create()
    vi_voices = voices.find(Language="vi")
    print("Các giọng tiếng Việt khả dụng:")
    for v in vi_voices:
        print(f"- {v['Name']} ({v['Gender']})")

async def test_tts():
    text = "Chào bạn, đây là bản thử nghiệm tốc độ của Edge TTS."
    voice = "vi-VN-HoaiMyNeural"
    output_file = "test_edge.mp3"
    communicate = edge_tts.Communicate(text, voice, rate="+25%")
    await communicate.save(output_file)
    print(f"Thành công! Đã tạo file {output_file}")

if __name__ == "__main__":
    try:
        asyncio.run(list_voices())
        asyncio.run(test_tts())
    except Exception as e:
        print(f"Lỗi: {e}")
