import logging
from ml_stage0.config import get_log_level, get_batch_size
from ml_stage0.features.cleaning import clean_age

ages = [25, -2, 32, 40, -1]

cleaned_ages = [clean_age(age) for age in ages]

print(cleaned_ages)

log_level = get_log_level()
batch_size = get_batch_size()

# ----------------- Logging -----------------
# logger configuration
logging.basicConfig(
    level=log_level,  # minimum log level
)
# create a logger
logger = logging.getLogger(__name__)

logger.info(f"ML_STAGE0_LOG_LEVEL: {log_level}")
logger.info(f"ML_STAGE0_BATCH_SIZE: {batch_size}")

logger.debug(f"Raw ages before cleaning: {ages}")
logger.debug(f"Cleaned ages: {cleaned_ages}")
