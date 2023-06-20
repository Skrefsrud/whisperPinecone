import whisper
from dotenv import load_dotenv

load_dotenv()

model = whisper.load_model("small.en")

PATH = "preTranscript/motivation.mp3"

result = model.transcribe(PATH)

f = open("postTranscript/motivation.txt", "a")
f.write(result["text"])