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

print(timediff(), "Generating zh ...")
tts.tts_to_file(
    text="清晨的微风温柔，带着盛开的花香。鸟儿们欢快地鸣叫，迎接新的一天。街道上逐渐热闹起来，人们开始了他们的日常生活。", 
    speaker_wav="KITT.wav", 
    language="zh", 
    file_path="output_zh.wav"
)
# Needs 5 seconds

print(timediff(), "Generating ja ...")
tts.tts_to_file(
    text="朝のそよ風は穏やかで、咲き誇る花の香りを運んでいました。鳥たちは楽しげにさえずり、新しい一日を迎えていました。通りは、日常の活動を始める人々でゆっくりと賑わい始めました。", 
    speaker_wav="KITT.wav", 
    language="ja", 
    file_path="output_ja.wav"
)
# Needs 5 seconds

print(timediff(), "Generating ar ...")
tts.tts_to_file(
    text="كانت نسيم الصباح لطيفًا، يحمل رائحة الأزهار المتفتحة. كانت الطيور تزقزق بسعادة، ترحب باليوم الجديد. كانت الشوارع تزدحم ببطء بالناس الذين يبدأون روتينهم اليومي.", 
    speaker_wav="KITT.wav", 
    language="ar", 
    file_path="output_ar.wav"
)
# Needs 5 seconds 

quit()

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

print(timediff(), "Generating pt ...")
tts.tts_to_file(
    text="Indexador e Processador de Evidências Digitais", 
    speaker_wav="KITT.wav", 
    language="pt", 
    file_path="output_pt.wav"
)
# Needs 28 seconds, real time factor 0.66

print(timediff(), "DONE")
