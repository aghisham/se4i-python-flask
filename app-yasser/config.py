import logging
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.yaml')

DEBUG = bool(os.getenv('debug'))
MODE = str(os.getenv('mode'))

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filename='logs/log.log')