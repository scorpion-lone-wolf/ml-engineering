import logging
from ml_stage0.config import get_log_level, get_batch_size
from ml_stage0.features.cleaning import clean_age

log_level = get_log_level()
batch_size = get_batch_size()


# logger configuration
logging.basicConfig(
    level=log_level,  # minimum log level
)
# create a logger
logger = logging.getLogger(__name__)


logger.info("ML_STAGE0_LOG_LEVEL: %s", log_level)
logger.info("ML_STAGE0_BATCH_SIZE: %s ", batch_size)

ages = [25, -2, 32, 40, -1]

logger.debug("Raw ages before cleaning: %s", ages)

cleaned_ages = [clean_age(age) for age in ages]

logger.debug("Cleaned ages: %s", cleaned_ages)

print(cleaned_ages)
