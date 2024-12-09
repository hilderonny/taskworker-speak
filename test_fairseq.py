from TTS.api import TTS
api = TTS(model_name="tts_models/deu/fairseq/vits").to("cuda")
api.tts_to_file("This is a test.", file_path="output_fairseq_deu_default.wav")

# TTS with on the fly voice conversion
api = TTS("tts_models/deu/fairseq/vits")
api.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="KITT.wav",
    file_path="ouptut_fairseq_deu_KITT.wav"
)