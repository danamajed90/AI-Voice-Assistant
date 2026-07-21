import whisper
import cohere
from gtts import gTTS

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Converting audio to text...")

result = model.transcribe("Recording4.wav", language="ar")

print("Recognized text:")
text = result["text"]
print("User:", text)
co = cohere.ClientV2(api_key="COHERE_API_KEY")

response = co.chat(
    model="command-r7b-arabic-02-2025",
    messages=[
        {
            "role": "user",
            "content": text
        }
    ]
)

reply = response.message.content[0].text

print("AI:", reply)
from gtts import gTTS

tts = gTTS(text=reply, lang="ar")
tts.save("output.mp3")

print("Audio saved as output.mp3")

print(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)