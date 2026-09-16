import os

DEFAULT_LOG_LEVEL = "INFO"


def get_log_level() -> str:
    return os.getenv("ML_STAGE0_LOG_LEVEL", DEFAULT_LOG_LEVEL)


DEFAULT_BATCH_SIZE = 32


def get_batch_size() -> int:
    raw_value = os.getenv("ML_STAGE0_BATCH_SIZE")

    if raw_value is None:
        return DEFAULT_BATCH_SIZE

    try:
        batch_size = int(raw_value)
    except ValueError as exc:
        raise ValueError(f"ML_STAGE0_BATCH_SIZE={raw_value} is not an integer")
    if batch_size <= 0:
        raise ValueError(f"ML_STAGE0_BATCH_SIZE={raw_value} is not positive")

    return batch_size
