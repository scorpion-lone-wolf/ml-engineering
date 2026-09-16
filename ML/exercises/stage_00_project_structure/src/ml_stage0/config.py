import os

DEFAULT_LOG_LEVEL = "INFO"


def get_log_level() -> str:
    return os.getenv("ML_STAGE0_LOG_LEVEL", DEFAULT_LOG_LEVEL)
