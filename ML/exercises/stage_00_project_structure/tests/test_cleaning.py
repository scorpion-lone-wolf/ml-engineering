from ml_stage0.features.cleaning import clean_age


def test_clean_age_returns_valid_age():
    # Arrange
    age = 25

    # Act
    cleaned_age = clean_age(age)

    # Assert
    assert cleaned_age == 25
