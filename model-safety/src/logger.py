import logging
import os
from datetime import datetime

RUN_TS = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
log_file = f"{RUN_TS}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, log_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)