# Directly use whisper to transcribe the audio file. Update the audio file below to match the file you placed into this folder.
import whisper
model = whisper.load_model("small")
result = model.transcribe("INPUT.m4a")
print(result["text"])