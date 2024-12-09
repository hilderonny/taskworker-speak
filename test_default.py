import time
import os

os.environ["TTS_HOME"] = "./data"

ct = time.time()

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

print(timediff(), "Initialize TTS ...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS

print(timediff(), "Default voice ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    language="de", 
    file_path="output_DEFAULT.wav"
)

print(timediff(), "DONE")
