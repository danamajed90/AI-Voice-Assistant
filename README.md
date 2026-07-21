# AI-Voice-Assistant
This project is a simple AI Voice Assistant developed using Python. It demonstrates the complete pipeline of speech processing by converting spoken audio into text, generating an intelligent response using a Large Language Model (LLM), and converting the generated response back into speech.

# Project Structure

```
VoiceAssistant/
─ main.py
─ Recording4.wav
─ output.txt
─ output.mp3
─ README.md
```
# Technologies Used

- Python
- OpenAI Whisper (Speech-to-Text)
- Cohere API (Large Language Model)
- Google Text-to-Speech (gTTS)
- FFmpeg

# Required Libraries

Install the required libraries before running the project.

```bash
pip install openai-whisper
pip install torch
pip install cohere
pip install gTTS
```
 FFmpeg Installation

Whisper requires FFmpeg to process audio files.

1. Download FFmpeg.
2. Extract the downloaded folder.
3. Add the **bin** folder to the system PATH.
4. Restart Visual Studio Code.

# Cohere API Key

Before running the project, replace:

```python
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

with your own Cohere API key.

# Running the Project

Run the following command:

```bash
python main.py
```
<img width="1920" height="1080" alt="Screenshot (231)" src="https://github.com/user-attachments/assets/fcc4be20-d7e7-402b-921e-2f7721c12a8a" />

# Generated Files

## output.txt
<img width="1296" height="561" alt="Screenshot (236)" src="https://github.com/user-attachments/assets/e2555970-8639-4327-9d42-c40a691790fc" />


## output.mp3

<img width="1621" height="561" alt="Screenshot (232)" src="https://github.com/user-attachments/assets/201559c1-4dee-4ccb-9058-4f175153a20b" />
