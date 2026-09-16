def clean_age(age: int) -> int | None:
    if age < 0:
        return None

    return age
