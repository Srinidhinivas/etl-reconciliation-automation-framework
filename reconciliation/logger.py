import logging
import os

from datetime import datetime


class FrameworkLogger:

    @staticmethod
    def setup_logger():

        log_folder = "logs"

        os.makedirs(
            log_folder,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%d-%m-%Y-%H-%M"
        )

        log_file = os.path.join(
            log_folder,
            f"recon_{timestamp}.log"
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        return logging