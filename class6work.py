from pathlib import Path
import pandas as pd

data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)

print(df.shape) # returns (number of rows, number of columns)

#You can access each value separately
rows = df.shape[0]
columns = df.shape[1]

print(df.head()) # displays the first five rows by default.
print(df.head(10)) # displays the first ten rows.
print(df.tail()) # displays the last five rows.

print(list(df.columns)) # displays the list of column names.

df.info() # displays Column names, Non-null counts, Data types, and Memory usage

print(df.describe()) # displays the summary of numeric columns.
# or print(df["release_year"].describe())

print(df.sample(5)) # randomly selects 5 samples
# or print(df.sample(5, random_state=1))

"""
print(df.shape) 
print(df.head())
print(df.columns) 
print(df.dtypes) 
df.info() 
print(df.describe())
"""

print(df.dtypes)

is_numeric = pd.api.types.is_numeric_dtype(df["viewer_score"])
print(is_numeric)
is_numeric = pd.api.types.is_numeric_dtype(df["title"])
print(is_numeric)

before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before-after} duplicate rows.")