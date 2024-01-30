import os
import logging
from administer_files import read_env
from method import check_os


def search_devices():
    if check_os():
        router_ip = read_env("router")
        logging.debug(f"got {router_ip}")
        while True:
            logging.info("scan started")
            os.system(f"sudo nmap -v {router_ip}/24 -oX files/devices.xml")
            logging.info("scan completed")
    elif not check_os():
        logging.warning("abort scan")
