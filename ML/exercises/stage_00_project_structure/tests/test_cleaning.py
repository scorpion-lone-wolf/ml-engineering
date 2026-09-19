from ml_stage0.features.cleaning import clean_age


def test_clean_age_returns_valid_age():
    # Arrange
    age = 25

    # Act
    cleaned_age = clean_age(age)

    # Assert
    assert cleaned_age == 25


def test_clean_age_returns_none_for_negative_age():
    # Arrange
    age = -25

    # Act
    cleaned_age = clean_age(age)

    # Assert
    assert cleaned_age is None


def test_clean_age_keeps_zero():
    # Arrange
    age = 0

    # Act
    cleaned_age = clean_age(age)

    # Assert
    assert cleaned_age == 0
