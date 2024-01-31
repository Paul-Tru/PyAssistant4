import sys
import logging


def check_os():
    current_os = sys.platform
    logging.debug(f"get current OS")
    if current_os == "Linux":
        logging.info(f"OS can handle nmap ({current_os})")
        return True
    else:
        logging.warning(f"OS can't handle nmap ({current_os})")
        return False
