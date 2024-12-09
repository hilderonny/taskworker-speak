from importlib.metadata import version
import time
import json
import requests
import datetime
import argparse
import os
import torch
import base64
from TTS.api import TTS
from pydub import AudioSegment

REPOSITORY = "https://github.com/hilderonny/taskworker-speak"
VERSION = "1.0.0"
LIBRARY = "TTS-" + version("TTS")
MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"
LOCAL_MODEL_PATH = "./data"
INTERMEDIATE_WAV_PATH = "intermediate.wav"
INTERMEDIATE_MP3_PATH = "intermediate.mp3"

print(f'taskworker-speak Version {VERSION}')

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--taskbridgeurl', type=str, action='store', required=True, help='Root URL of the API of the task bridge to use, e.g. https://taskbridge.ai/')
parser.add_argument('--device', type=str, action='store', required=True, help='Device to use for processing. Can be "cpu", "cuda" or "cuda:0"')
parser.add_argument('--version', '-v', action='version', version=VERSION)
parser.add_argument('--worker', type=str, action='store', required=True, help='Unique name of this worker')
args = parser.parse_args()

WORKER = args.worker
print(f'Worker name: {WORKER}')
TASKBRIDGEURL = args.taskbridgeurl
if not TASKBRIDGEURL.endswith("/"):
    TASKBRIDGEURL = f"{TASKBRIDGEURL}/"
APIURL = f"{TASKBRIDGEURL}api/"
print(f'Using API URL {APIURL}')

DEVICE = args.device
if not torch.cuda.is_available():
    DEVICE = "cpu"
print(f'Using device {DEVICE}')

os.environ["TTS_HOME"] = "./data"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(DEVICE)

def report_progress(taskid, progress):
    body = {
        "progress": str(progress)
    }
    requests.post(f"{APIURL}tasks/progress/{taskid}/", json=body)

def check_and_process():
    start_time = datetime.datetime.now()
    take_request = {}
    take_request["type"] = "speak"
    take_request["worker"] = WORKER
    req = requests.post(f"{APIURL}tasks/take/", json=take_request)
    if req.status_code != 200:
        return False
    task = req.json()
    taskid = task["id"]
    print(json.dumps(task, indent=2))
    language = "de"
    voice = "KITT"
    if "language" in task["data"]:
        language = task["data"]["language"]
    if "voice" in task["data"]:
        voice = task["data"]["voice"]
    speaker_wav = voice + ".wav"
    texts_to_speak = task["data"]["texts"]
    result_to_report = {}
    result_to_report["result"] = {}
    text_to_speak = "\n".join(texts_to_speak)

    result_element = ""
    if len(text_to_speak) < 1:
        result_element = ""
    else:
        # try:
        # Create audio
        tts.tts_to_file(text=text_to_speak, speaker_wav=speaker_wav, language=language, file_path=INTERMEDIATE_WAV_PATH)
        # Convert to MP3
        audio = AudioSegment.from_wav(INTERMEDIATE_WAV_PATH)
        audio.export(INTERMEDIATE_MP3_PATH, format="mp3")
        # Convert to Base64
        with open(INTERMEDIATE_MP3_PATH, 'rb') as fmp3:
            b64 = base64.b64encode(fmp3.read())
            print(b64)
            result_element = b64.decode('utf-8')
        # except ex:
        #     print(ex)
        #     pass
    result_to_report["result"]["audio"] = result_element

    end_time = datetime.datetime.now()
    result_to_report["result"]["device"] = DEVICE
    result_to_report["result"]["duration"] = (end_time - start_time).total_seconds()
    result_to_report["result"]["repository"] = REPOSITORY
    result_to_report["result"]["version"] = VERSION
    result_to_report["result"]["library"] = LIBRARY
    result_to_report["result"]["model"] = MODEL
    #print(json.dumps(result_to_report, indent=2))
    #print("Reporting result")
    requests.post(f"{APIURL}tasks/complete/{taskid}/", json=result_to_report)
    #print("Done")
    return True

try:
    print('Ready and waiting for action')
    while True:
        text_was_processed = False
        try:
            text_was_processed = check_and_process()
        except Exception as ex:
            print(ex)
        if text_was_processed == False:
            time.sleep(3)
except Exception:
    pass
