import os
from dotenv import load_dotenv
import logging


def read_env(variable):
    # Path to env file in data
    env_path = '/files/CONFIG.env'

    # Load env
    load_dotenv(dotenv_path=env_path)

    # Get Variable
    env = os.getenv(variable)
    logging.debug(f"Get {variable} variable from env file ({env})")
    return env
