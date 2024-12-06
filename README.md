# taskworker-speak

## Installation

For windows first install "Microsoft C++ Build Tools" from https://visualstudio.microsoft.com/de/visual-cpp-build-tools/.
This is required for TTS installation. Do not tick additional options within the installer (should show only 138 MB to install).

Next install Python 3.9 (CoquiTTS requires >=3.8 <3.11)

### Windows

```sh
pip install git+https://github.com/coqui-ai/TTS  # from Github


#pip install torch==2.3.0 --index-url https://download.pytorch.org/whl/cu118
pip install numpy Cython
pip install TTS==0.22.0
```

### Raspberry

````sh
sudo apt update
sudo apt upgrade
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim

wget https://www.python.org/ftp/python/3.9.21/Python-3.9.21.tgz
tar zxf Python-3.9.21.tgz
cd Python-3.9.21
./configure --enable-optimizations
make -j 4
sudo make altinstall
sudo python3.9 -m pip install --upgrade pip

python3.9 -m venv python-venv
source python-venv/bin/activate

pip install TTS==0.22.0
```

Model: C:\Users\XXXXXX\AppData\Local\tts\tts_models--multilingual--multi-dataset--xtts_v2

Set model path: https://github.com/coqui-ai/TTS/discussions/2476