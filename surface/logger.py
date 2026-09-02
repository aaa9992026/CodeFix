import logging
import os

# directory of this file
BASE_DIR = os.path.dirname(__file__)

# logs directory
LOG_DIR = os.path.join(BASE_DIR, "logs")

# make sure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# reduce library noise
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)