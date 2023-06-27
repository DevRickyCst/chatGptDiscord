from io import BytesIO

from gtts import gTTS


class GoogleTTS:
    def __init__(self) -> None:
        pass

    def get_audio_fp(text, lang="fr"):
        audio_fp = BytesIO()
        gTTS(text=text, lang=lang, slow=False).write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
