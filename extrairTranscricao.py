# instalar openai-whisper
# instalar ffmpeg: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
import whisper

# Carrega o modelo Whisper (você pode escolher entre tiny, base, small, medium, large)
model = whisper.load_model("medium")

# Defina o caminho para o arquivo de áudio que deseja transcrever
audio_path = "podcast.mp3"  # Substitua pelo caminho do seu arquivo de áudio

# Realiza a transcrição
result = model.transcribe(audio_path)

# Exibe o texto transcrito
print(result["text"])

# Opcional: Salvar a transcrição em um arquivo de texto
with open("transcricoes/gabriel.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
