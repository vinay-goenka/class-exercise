import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    # TODO 1:
    # Load filepath using pd.read_csv().
    # Log an INFO.
    # Return the DataFrame.
    df = pd.read_csv(filepath)
    logger.info(f"Data loaded from {filepath}")
    return df
