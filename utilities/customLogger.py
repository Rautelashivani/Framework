import logging
import os
from datetime import datetime


class LogGen:
    @staticmethod
    def loggen():
        # Create Logs directory if it doesn't exist
        log_dir = ".\\Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a unique log file for each test run
        log_file = os.path.join(log_dir, f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True  # Override any existing handlers
        )

        logger = logging.getLogger()
        return logger