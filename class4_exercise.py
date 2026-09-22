import os
from pathlib import Path

# Messy string concatenation
data_dir = 'data'
filename = 'sales.csv'

# Only works on Mac/Linux!
file_path = data_dir + '/' + filename  
# Only works on Windows
file_path = data_dir + '\\' + filename

# Clean object-oriented approach
data_dir = Path('data')
file_path = data_dir / 'sales.csv'  # Works everywhere!

# Check if exists
if file_path.exists():
    print("File exists")

# Get extension
ext = file_path.suffix  # '.csv'
