import logging
import os
from datetime import datetime

RUN_TS = datetime.now().strftime("%Y_%m_%d_%H%M%S")


def set_logger(prefix: str = None, log_level: str = "info"):
    log_file = f"{prefix}_{RUN_TS}.log"
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(logs_path, log_file)

    # Map log_level to logging level
    if log_level.lower() == "debug":
        logging_level = logging.DEBUG
    elif log_level.lower() == "info":
        logging_level = logging.INFO
    elif log_level.lower() == "warning":
        logging_level = logging.WARNING
    elif log_level.lower() == "error":
        logging_level = logging.ERROR
    elif log_level.lower() == "critical":
        logging_level = logging.CRITICAL
    else:
        logging_level = logging.INFO

    logging.getLogger().setLevel(logging_level)
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging_level,
    )
