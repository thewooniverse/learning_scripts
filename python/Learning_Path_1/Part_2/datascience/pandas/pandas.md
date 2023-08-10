-> learn translating dataframes into csvs, xmls and using SQL on them as well.

=========================================================================
Overview Notes
=========================================================================

Sure! Pandas is a powerful library for data manipulation and analysis in Python. It's built on top of NumPy, and its key data structures are Series and DataFrame.

### Series
A Series is a one-dimensional labeled array capable of holding any data type. You can think of it as a specialized dictionary or a generalized NumPy array.

```python
import pandas as pd

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print(s)
```

### DataFrame
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or a SQL table.

```python
data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
        'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data)
print(df)
```

### Importing and Exporting Data
Pandas can import data from various formats like CSV, Excel, JSON, SQL, etc.

```python
# Reading from a CSV file
df = pd.read_csv('file.csv')

# Writing to an Excel file
df.to_excel('file.xlsx')
```

### Selection
You can select data using column names, row numbers, or conditions.

```python
# Select a column by name
capital_column = df['Capital']

# Select multiple columns by names
subset = df[['Country', 'Capital']]

# Select rows by position
rows = df.iloc[0:2]
```

### Filtering
Filtering can be done using boolean conditions.

```python
# Filter by condition
large_population = df[df['Population'] > 100000000]
```

### Aggregation
You can perform various aggregation operations like sum, mean, etc.

```python
# Calculate mean of the population
mean_population = df['Population'].mean()
```

### Merging and Joining
Pandas provides various ways to combine DataFrames, like merge and concat.

```python
# Concatenating two DataFrames
combined = pd.concat([df1, df2])

# Merging two DataFrames on a common column
merged = pd.merge(df1, df2, on='key')
```

### Handling Missing Data
Pandas provides methods for handling missing data.

```python
# Drop missing values
df.dropna()

# Fill missing values
df.fillna(value=0)
```

### Plotting
Pandas integrates with Matplotlib for basic plotting.

```python
df['Population'].plot(kind='bar')
```

These are some of the basics to get you started with Pandas. There's a lot more to explore, and the [Pandas documentation](https://pandas.pydata.org/docs/) is a great place to delve deeper.











=========================================================================
Targeting / indexing dataframes
=========================================================================
Indexing and targeting specific elements in a Pandas DataFrame can be achieved through various methods. Here's an overview:

### 1. Using Column Names:

You can access a specific column by its name.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
column_a = df['A']
```

### 2. Using `.loc[]` for Label-Based Indexing:

The `.loc[]` method is used to access a group of rows and columns by their labels or a boolean array.

```python
row_1 = df.loc[0]       # Accessing the first row
cell_A1 = df.loc[0, 'A']  # Accessing the first row of column 'A'
```

### 3. Using `.iloc[]` for Positional Indexing:

The `.iloc[]` method is used for indexing by integer location. You can use this to access rows and columns by their integer index.

```python
row_1 = df.iloc[0]       # Accessing the first row
cell_A1 = df.iloc[0, 0]  # Accessing the first row of the first column
```

### 4. Using Boolean Masking:

You can also use conditions to filter the DataFrame and access specific elements.

```python
mask = df['A'] > 1
filtered_rows = df[mask]  # Accessing rows where the value in column 'A' is greater than 1
```

### 5. Slicing:

Slicing allows you to access a range of rows or columns.

```python
first_two_rows = df[:2]  # Accessing the first two rows
```

### 6. Using `.at[]` and `.iat[]`:

These methods provide fast access to a single element.

```python
cell_A1 = df.at[0, 'A']    # Accessing element by row label and column name
cell_A1 = df.iat[0, 0]     # Accessing element by row and column index
```

These are some common ways to index and target specific elements, rows, or columns in a Pandas DataFrame. Depending on the situation and the nature of the index (whether it's an integer or a label), you may choose the method that best suits your needs.







=========================================================================
df.dropna()
=========================================================================

The `dropna` method in Pandas doesn't actually replace any values; instead, it removes missing values from a DataFrame. Depending on how it's used, it can remove any row or column that contains at least one missing value (NaN or None).

Here's a quick overview of how `dropna` can be used:

- `dropna()`: Removes any row that contains at least one missing value.
- `dropna(axis=1)`: Removes any column that contains at least one missing value.
- `dropna(how='all')`: Removes rows where all the elements are missing.
- `dropna(subset=['column_name'])`: Removes rows where the specified column(s) have missing values.

The DataFrame returned by `dropna` is a new DataFrame with the missing values removed, and it doesn't modify the original DataFrame unless the `inplace` parameter is set to True.

Here's an example:

```python
import pandas as pd
import numpy as np

# Creating a DataFrame with some NaN values
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, 1]
})

# Using dropna() to remove rows with any NaN values
cleaned_df = df.dropna()

print(cleaned_df)
```

The output would be:

```
     A    B
0  1.0  5.0
```

Row 1 and 2 from the original DataFrame were removed because they contained at least one NaN value.














=========================================================================
Generalized Meaning
=========================================================================
In the context of the explanation about Pandas' Series being a "generalized NumPy array," the term "generalized" means that the Series object extends or broadens the concept of a NumPy array by adding more functionality and flexibility.

A NumPy array is a homogeneous n-dimensional array, meaning that all elements must be of the same type. It uses integer indices to access the elements.

On the other hand, a Pandas Series, while still being a one-dimensional array, can have labels (indices) of any hashable type, not just integers, and can contain mixed data types. This makes it more versatile and adaptable to different use cases.

In this sense, the Pandas Series is a more general or broadened version of a NumPy array, capable of handling a wider variety of scenarios and data structures. That's what "generalized" refers to in this context.

