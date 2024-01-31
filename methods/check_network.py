import urllib.request
import logging


def check_network(link=None):
    if not link:
        link = "google.com"
    try:
        logging.debug(f"ping {link}")
        urllib.request.urlopen(f'http://www.{link}', timeout=1)
        logging.info("Connected")
    except urllib.error.URLError:
        logging.warning("L.O.S.")
