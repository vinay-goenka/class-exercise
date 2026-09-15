import argparse
import csv
import sys
from pathlib import Path
import logging


def check_data(filename):
    """Read the CSV file and check for missing values."""
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if not rows:
            return [], [], []
        header = rows[0]
        data = rows[1:]
        missing_rows = []
        for row_number, row in enumerate(data, start=2):
            if any(value == "" for value in row):
                missing_rows.append(row_number)
    return header, data, missing_rows

parser = argparse.ArgumentParser(
    description='Check the quality of a CSV data file'
    )
parser.add_argument(
    "--input", 
    "-i",
    required=True,
    help="CSV file to check"
    )

parser.add_argument(
    "--output", 
    "-o", 
    default="data_quality.txt", 
    help="Output report filename"
    )

parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Show detailed DEBUG messages"
    )

p = Path(args.input)
if not p.is_file():
    print(f"File not found: '{args.input}'")
    sys.exit(1)

print(f"File validated: '{args.input}'")

header, data, missing_rows = check_data(args.input)

with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
    )
# Create a module-level logger
logger = logging.getLogger(__name__)

args = parser.parse_args()
if args.verbose:
    logger.setLevel(logging.DEBUG)

logger.debug(f"Arguments parsed: filename={args.input}")
    
logger.info(f"File validated: '{args.input}'")

logger.debug(f"Loading data from: '{args.input}'")
