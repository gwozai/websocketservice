import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

SERVER_ADDRESS = os.getenv("SERVER_ADDRESS", config.get('Server', 'address', fallback="localhost"))
SERVER_PORT = int(os.getenv("SERVER_PORT", config.get('Server', 'port', fallback=8765)))
LOG_LEVEL = os.getenv("LOG_LEVEL", config.get('Logging', 'level', fallback="INFO"))
