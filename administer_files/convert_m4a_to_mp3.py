from pydub import AudioSegment
import os
import logging


def convert_m4a_to_mp3(input_file, output_file):
    if os.path.exists(input_file):
        convert_m4a_to_mp3(input_file, output_file)
        logging.debug(f"'{input_file}': file exists")
    else:
        logging.warning(f"'{input_file}': file doesn't exist")

    audio = AudioSegment.from_file(input_file, format="m4a")

    audio.export(output_file, format="mp3")
    logging.info(f"converted '{input_file}' into '{output_file}'")
