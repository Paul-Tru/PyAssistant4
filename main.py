import logging
# from method import search_devices
from administer_files import read_env

# Logging Config
logging.basicConfig(format="%(levelname)s [%(asctime)s] (%(funcName)s): %(message)s",
                    datefmt="%d/%m/%Y %H:%M:%S",
                    level=logging.DEBUG,
                    filename="log.txt")


def main():
    logging.info("program started")
    # search_devices()
    # logging.info("called func: search_devices")
    read_env("router")


if __name__ == '__main__':
    main()
