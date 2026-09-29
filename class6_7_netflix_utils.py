import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f"DF shape: {df.shape}")
    print(df.shape)
    print(df.head(5))
    print(df.columns)
    print(df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before = len(df)
    after = len(df.drop_duplicates())
    logger.debug(f"Before: {before}. After removing duplicates: {after}")
    new_df = df.drop_duplicates()
    return new_df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before = len(df)
    after = len(df.dropna())
    logger.debug(f"Before: {before}. After dropping missing rows: {after}")
    new_df = df.dropna()
    return new_df
