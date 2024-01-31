import logging
from methods import search_devices, check_network
# from administer_files import convert_m4a_to_mp3, manage_ini, read_env


# Logging Config
logging.basicConfig(format="%(levelname)s [%(asctime)s] (%(funcName)s): %(message)s",
                    datefmt="%d/%m %H:%M:%S",
                    level=logging.DEBUG,
                    filename="files/log.txt")


def main():
    logging.info("started")


if __name__ == '__main__':
    main()
    check_network()

