# taskworker-speak

## Installation

https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst

Model: C:\Users\XXXXXX\AppData\Local\tts\tts_models--multilingual--multi-dataset--xtts_v2

Set model path: https://github.com/coqui-ai/TTS/discussions/2476


## Installation


Make sure to install the CUDA Toolkit 11.8 from https://developer.nvidia.com/cuda-11-8-0-download-archive.

Install Python 3.11. The run the following commands in the folder of the downloaded repository.

```sh
python3.11 -m venv python-venv
python-venv\Scripts\activate # Windows
source ./python-venv/bin/activate # Linux
pip install torch==2.4.1 --index-url https://download.pytorch.org/whl/cu118
pip install TTS==0.22.0 cutlet==0.4.0 unidic==1.1.0
python -m unidic download
```

Downloads about 4 GB.
