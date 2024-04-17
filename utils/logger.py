import logging
from config.config import LOG_LEVEL


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger
