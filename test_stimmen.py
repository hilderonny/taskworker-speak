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

print(timediff(), "KITT ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="KITT.wav", 
    language="de", 
    file_path="output_KITT.wav"
)

print(timediff(), "MERKEL ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="MERKEL.wav", 
    language="de", 
    file_path="output_MERKEL.wav"
)

print(timediff(), "SCHOLZ ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="SCHOLZ.wav", 
    language="de", 
    file_path="output_SCHOLZ.wav"
)

print(timediff(), "IRONMAN ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="IRONMAN.wav", 
    language="de", 
    file_path="output_IRONMAN.wav"
)

print(timediff(), "WILLIS ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="WILLIS.wav", 
    language="de", 
    file_path="output_WILLIS.wav"
)

print(timediff(), "SPONGEBOB ...")
tts.tts_to_file(
    text="In Deggendorf in Niederbayern ist wegen des Hochwassers ein Passagierschiff evakuiert worden. Mehr als 140 Menschen würden seit den Mittagsstunden vom Schiff gebracht, sagte eine Sprecherin des Landratsamts am Montag. Wegen des Hochwassers an der Donau könne das Schiff nicht weiterreisen. Bei den Passagieren handle es sich überwiegend um ältere Menschen. Es gebe aber bislang keinen medizinischen Notfall an Bord, hieß es weiter. Boote waren im Einsatz, um die Menschen an Land zu bringen.", 
    speaker_wav="SPONGEBOB.wav", 
    language="de", 
    file_path="output_SPONGEBOB.wav"
)

print(timediff(), "DONE")
