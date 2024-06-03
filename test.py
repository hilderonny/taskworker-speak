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
# Text to speech to a file
print(timediff(), "Generating en ...")
tts.tts_to_file(
    text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.", 
    speaker_wav="KITT.wav", 
    language="en", 
    file_path="output_en.wav"
)
# Needs 5 seconds, real time factor 0.64

print(timediff(), "Generating de ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="KITT.wav", 
    language="de", 
    file_path="output_de.wav"
)
# Needs 28 seconds, real time factor 0.66

print(timediff(), "Generating ru ...")
tts.tts_to_file(
    text="Для России характерны самые разнообразные типы и формы рельефа, встречающиеся в природе. Господствующим типом рельефа, занимающим почти ¾ территории страны, являются равнины. Особенно выделяются Восточно-Европейская и Западно-Сибирская – крупнейшие равнины земного шара.", 
    speaker_wav="KITT.wav", 
    language="ru", 
    file_path="output_ru.wav"
)
# Needs 12 seconds, real time factor 0.51

print(timediff(), "DONE")
