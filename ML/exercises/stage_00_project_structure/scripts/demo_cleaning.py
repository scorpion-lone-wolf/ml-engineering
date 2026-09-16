from ml_stage0.config import get_log_level
from ml_stage0.features.cleaning import clean_age

ages = [25, -2, 32, 40, -1]

cleaned_ages = [clean_age(age) for age in ages]

print(cleaned_ages)

log_info = get_log_level()
print("ML_STAGE0_LOG_LEVEL:", log_info)
