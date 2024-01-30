import sys
import logging


def check_os():
    current_os = sys.platform
    logging.debug(f"get current OS")
    if current_os == "Linux":
        logging.info(f"current OS can handle nmap ({current_os})")
        return True
    else:
        logging.warning(f"current OS can not handle nmap. Please switch to a linux distribution ({current_os})")
        return False
