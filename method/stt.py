import whisper
from administer_files.manage_ini import read_ini
import logging


def whisper_stt(path):
    model_config = read_ini("whisper", "model")
    logging.debug(f"get model: {model_config}")

    language_config = read_ini("whisper", "language")
    logging.debug(f"get language: {language_config}")

    options = {"language": language_config}
    model = whisper.load_model(model_config)

    logging.info("transcription started")
    res = model.transcribe(path, **options)
    logging.info("transcription finished")
    return res["text"]
