import logging
from pathlib import Path

from utils.config import LOGS_DIR


def get_logger(name):
    LOGS_DIR.mkdir(exist_ok=True)
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(message)s")

    file_handler = logging.FileHandler(LOGS_DIR / "test_execution.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
