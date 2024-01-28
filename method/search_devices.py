import os
import logging
from administer_files import read_env


def search_devices():
    router_ip = read_env("router")
    while True:
        logging.info("scan started")
        os.system(f"sudo nmap -v {router_ip}/24 -oX devices.xml")
        logging.info("scan completed")
