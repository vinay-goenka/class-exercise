import pandas as pd
import pytest

from class10_data_validator import validate_columns


@pytest.fixture
def sample_df():
    """Create a small DataFrame for testing."""
    return pd.DataFrame(
        {
            "title": ["Movie A", "Movie B"],
            "type": ["Movie", "Movie"],
            "release_year": [2020, 2021],
        }
    )


def test_validate_columns_with_valid_columns(sample_df):
    required_columns = ["title", "type", "release_year"]
    validated_df = validate_columns(sample_df, required_columns)
    assert list(validated_df.columns) == required_columns


def test_validate_columns_with_missing_column(sample_df):
    # TODO 2:
    # Use pytest.raises() to confirm that validate_columns()
    # raises ValueError when a required column is missing.
    pytest.raises(ValueError, match="Missing required columns: \['director'\]")(
        validate_columns, sample_df, ["title", "type", "release_year", "director"]
    )