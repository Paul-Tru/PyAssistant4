import logging
from method import search_devices, stt
from administer_files import convert_m4a_to_mp3, manage_ini, read_env


# Logging Config
logging.basicConfig(format="%(levelname)s [%(asctime)s] (%(funcName)s): %(message)s",
                    datefmt="%d/%m/%Y %H:%M:%S",
                    level=logging.DEBUG,
                    filename="files/log.txt")


def main():
    logging.info("program started")


if __name__ == '__main__':
    main()

