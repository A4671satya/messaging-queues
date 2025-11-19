import logging
from .config import settings

logger = logging.getLogger('demo_app')
logger.setLevel(logging.INFO)

handler = logging.FileHandler(settings.LOG_FILE)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
