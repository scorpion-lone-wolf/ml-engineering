import logging
from ml_stage0.config import get_log_level, get_batch_size
from ml_stage0.features.cleaning import clean_age

# create a logger
logger = logging.getLogger(__name__)


def main() -> None:
    log_level = get_log_level()
    batch_size = get_batch_size()
    # logger configuration
    logging.basicConfig(
        level=log_level,  # minimum log level
    )
    logger.info("ML_STAGE0_LOG_LEVEL: %s", log_level)
    logger.info("ML_STAGE0_BATCH_SIZE: %s ", batch_size)

    ages = [-25, -2, -32, -40, -1]

    logger.debug("Raw ages before cleaning: %s", ages)

    cleaned_ages = [clean_age(age) for age in ages]
    invalid_count = sum(x is None for x in cleaned_ages)

    if ages and len(ages) == invalid_count:
        logger.error("All ages are invalid")
    elif invalid_count > 0:
        logger.warning("Invalid age count: %s", invalid_count)

    logger.debug("Cleaned ages: %s", cleaned_ages)

    print(cleaned_ages)


if __name__ == "__main__":
    main()
