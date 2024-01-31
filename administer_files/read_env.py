import os
from dotenv import load_dotenv
import logging


def read_env(variable):
    # Path to env file in data
    env_path = 'files/CONFIG.env'

    # Load env
    load_dotenv(dotenv_path=env_path)
    logging.debug("load file")

    # Get Variable
    env = os.getenv(variable)
    logging.info(f"get '{variable}' from '{env}'")
    return env
