from TTS.api import TTS

tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="KITT.wav",
    file_path="ouptut_THORSTEN.wav"
)