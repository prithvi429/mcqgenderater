import logging
import os
from datetime import datetime  # Fixed import

# Correct strftime usage
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory
LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_PATH, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Fixed case
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
