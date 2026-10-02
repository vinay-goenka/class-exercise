import logging
import re
import sys
import pandas as pd

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


def clean_text(value):
    """Normalize one text value."""
    # TODO 1:
    # Strip surrounding whitespace.
    # Convert text to lowercase.
    # Collapse repeated whitespace.
    
    value = value.strip()
    value = value.lower()
    value = re.sub(r'\s+', ' ', value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    # If column does not exist:
    # Log an ERROR message and raise ValueError.
    # Calculate Q1, Q3, and IQR.
    # Use threshold to calculate lower and upper bounds.
    # Keep rows inside the bounds.
    # Log a DEBUG message containing the bounds and the number of rows removed.
    # Return the resulting DataFrame.
    
    if column not in df.columns:
        logger.error(f"Column '{column}' does not exist")
        raise ValueError(f"Column '{column}' does not exist")
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - threshold * iqr
    upper = q3 + threshold * iqr
    before = len(df)
    df = df[(df[column]>=lower) & (df[column]<=upper)]
    after = len(df)
    logger.debug(f"Lower bound: {lower}, Upper bound: {upper}. Rows removed: {before - after}")

    # TODO 3:
    # Inside a try block, remove runtime_minutes outliers
    # using remove_iqr_outliers() with a threshold of 1.5.
    # Catch ValueError and exit with sys.exit(1).# Log an INFO message.
    try:
        df = remove_iqr_outliers(df, 'runtime_minutes', 1.5)
    except ValueError as e:
        logger.error(f"Error removing outliers: {e}")
        sys.exit(1)

    # TODO 4:
    # Apply clean_text() to title, type, and country.
    # Log an INFO message.
    for col in ['title', 'type', 'country']:
        df[col] = df[col].apply(clean_text)

    # TODO 5:
    # Create a report (dictionary) containing rows_before, rows_after, rows_removed, and columns.
    # Log an INFO message reporting: rows_before, rows_after, rows_removed, and columns.
    rows_before = len(df)
    rows_after = len(df)
    rows_removed = rows_before - rows_after
    columns = df.columns.tolist()
    report = {
        'rows_before': rows_before,
        'rows_after': rows_after,
        'rows_removed': rows_removed,
        'columns': columns
    }
    logger.info(f"Report: {report}")