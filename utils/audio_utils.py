import wave
from config import SAMPLE_RATE, SAMPLE_WIDTH, CHANNELS

def save_frames_to_wav(frames, filename="buffer.wav"):
    if not frames:
        print("⚠️ No audio frames provided")
        return False

    frames_bytes = b"".join(frames)
    if not frames_bytes:
        print("⚠️ Audio frames are empty bytes")
        return False

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(frames_bytes)

    print(f"💾 Saved buffer to {filename}")
    return True

def load_system_prompt():
    with open("prompts/elara_system_prompt.txt", "r", encoding="utf-8") as f:
        return {"role": "system", "content": f.read()}