# utils/logger.py

import logging
import os
from datetime import datetime

def setup_logger(log_file_path=None, level=logging.INFO):
    # Default log path with timestamp if not provided
    if not log_file_path:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file_path = f"logs/test_log_{timestamp}.log"

    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(level)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
