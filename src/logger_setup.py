import logging

APP_NAME = "gibberish-detector"
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")

file_logging = logging.FileHandler(f"./logs/{APP_NAME}_dev.log")
file_logging.setFormatter(formatter)
logger.addHandler(file_logging)