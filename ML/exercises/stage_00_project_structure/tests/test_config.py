import pytest
from ml_stage0.config import get_batch_size


def test_get_batch_size_returns_default_if_env_missing(monkeypatch):
    # Arrange
    # raising false means , if it was already absent, don't raise error
    monkeypatch.delenv("ML_STAGE0_BATCH_SIZE", raising=False)
    # Act
    batch_size = get_batch_size()
    # Assert
    assert batch_size == 32


def test_get_batch_size_returns_env_value(monkeypatch):
    # Arrange
    monkeypatch.setenv("ML_STAGE0_BATCH_SIZE", "64")
    # Act
    batch_size = get_batch_size()
    # Assert
    assert batch_size == 64


def test_get_batch_size_returns_value_error_for_non_integer(monkeypatch):
    # Arrange
    monkeypatch.setenv("ML_STAGE0_BATCH_SIZE", "abc")
    # Act & Assert
    with pytest.raises(ValueError):
        get_batch_size()


def test_get_batch_size_returns_value_error_for_non_positive_integer(monkeypatch):
    # Arrange
    monkeypatch.setenv("ML_STAGE0_BATCH_SIZE", "-64")
    # Act & Assert
    with pytest.raises(ValueError):
        get_batch_size()
