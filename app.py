import whisper
from dotenv import load_dotenv

load_dotenv()

model = whisper.load_model("small.en")

PATH = "preTranscript/sleepShort.mp3"

result = model.transcribe(PATH)

f = open("preTranscript/sleepShort.txt", "a")
f.write(result["text"])