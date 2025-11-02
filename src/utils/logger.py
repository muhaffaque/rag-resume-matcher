import logging
import os
from datetime import datetime

def get_logger(name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d')}.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger(name)
