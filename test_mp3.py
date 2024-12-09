import time
import os
import base64

os.environ["TTS_HOME"] = "./data"

ct = time.time()

file_path_wav = "intermediate.wav"
file_path_mp3 = "output.mp3"
file_path_base64 = "output.base64.txt"

def timediff():
    global ct
    now = time.time()
    diff = now - ct
    ct = now
    return str(diff) + "\n"

# https://huggingface.co/coqui/XTTS-v2
# https://pypi.org/project/coqui-tts/

print(timediff(), "Importing Torch ...")
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)
print(timediff(), "Importing TTS ...")
from TTS.api import TTS
print(timediff(), "Importing Pydub ...")
from pydub import AudioSegment

print(timediff(), "Initialize TTS ...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

print(timediff(), "Generating WAV file ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="MERKEL.wav", 
    language="de", 
    file_path=file_path_wav
)

print(timediff(), "Converting to MP3 ...")
audio = AudioSegment.from_wav(file_path_wav)
audio.export(file_path_mp3, format="mp3")

print(timediff(), "Creating Base64 ...")
with open(file_path_mp3, 'rb') as fmp3:
    b64 = base64.b64encode(fmp3.read())
    with open(file_path_base64, 'wb') as ftxt:
        ftxt.write(b64)

print(timediff(), "DONE")
