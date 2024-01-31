import configparser
import logging

file_path = "files/config.ini"


def read_ini(sec, var):
    config = configparser.ConfigParser()
    config.read(file_path)
    logging.debug("load file")
    ini = config.get(sec, var)
    logging.info(f"get '{var}' from '{sec}' ({ini})")
    return ini


def write_ini(sec, var, content):
    config = configparser.ConfigParser()
    config.read(file_path)

    if not config.has_section(sec):
        config.add_section(sec)
        logging.debug("add new section")

    config.set(sec, var, content)

    with open(file_path, 'w') as config_file:
        config.write(config_file)
        logging.debug(f"write '{content}' into '{var}' '{sec}'")
