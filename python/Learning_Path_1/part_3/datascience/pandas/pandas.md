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
Overview / Usage pt 2
=========================================================================
Certainly! DataFrames are a part of the `pandas` library in Python, which is a powerful and popular tool for data analysis and manipulation.

### Basics:

A DataFrame is a 2-dimensional labeled data structure with columns that can be of different types, similar to a spreadsheet, SQL table, or a dictionary of series objects.

### Setting Up:

To work with DataFrames, first, you need to install and import the pandas library:

```bash
pip install pandas
```

```python
import pandas as pd
```

### Creating DataFrames:

1. **From a Dictionary**:

```python
data = {
    'name': ['John', 'Jane', 'Sam'],
    'age': [28, 24, 22],
    'city': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)
```

2. **From a List of Lists**:

```python
data = [['John', 28, 'New York'], ['Jane', 24, 'San Francisco'], ['Sam', 22, 'Los Angeles']]
df = pd.DataFrame(data, columns=['name', 'age', 'city'])
print(df)
```

### Accessing Data:

1. **Select a Column**:

```python
print(df['name'])
```

2. **Select Multiple Columns**:

```python
print(df[['name', 'city']])
```

3. **Select Rows using `.loc` and `.iloc`**:

```python
print(df.loc[0])  # Returns the first row
print(df.iloc[1])  # Returns the second row
```

### Modifying Data:

1. **Adding a Column**:

```python
df['job'] = ['Engineer', 'Designer', 'Manager']
```

2. **Deleting a Column**:

```python
df.drop('job', axis=1, inplace=True)
```

3. **Adding a Row**:

```python
new_row = {'name': 'Lucy', 'age': 30, 'city': 'Chicago'}
df = df.append(new_row, ignore_index=True)
```

### Basic Operations:

1. **Filter Data**:

```python
older_than_25 = df[df['age'] > 25]
print(older_than_25)
```

2. **Sorting Data**:

```python
sorted_by_age = df.sort_values(by='age')
print(sorted_by_age)
```

3. **Grouping Data**:

```python
group_by_city = df.groupby('city').size()
print(group_by_city)
```

4. **Handling Missing Data**:

```python
df['salary'] = [50000, None, 60000, 55000]
df.fillna(0, inplace=True)  # Replaces NaN values with 0
```

### Statistics:

```python
print(df.describe())  # Gives a summary of numerical columns
```

### Saving and Loading Data:

1. **To/From CSV**:

```python
df.to_csv('data.csv', index=False)
loaded_df = pd.read_csv('data.csv')
```

2. **To/From Excel**:

```python
df.to_excel('data.xlsx', index=False)
loaded_df = pd.read_excel('data.xlsx')
```

These are just the basics. `pandas` offers a plethora of functionalities to help you work efficiently with data in Python. If you find yourself working frequently with data, I highly recommend delving deeper into the `pandas` documentation and tutorials.










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
df.drop()
=========================================================================
Certainly! This line of code pertains to the manipulation of a DataFrame (`df`) using the `pandas` library in Python.

Here's a breakdown of the function:

### `df.drop(...)`

The `drop` method of a DataFrame is used to drop specified labels from rows or columns. 

### `'job'`

This specifies which label you want to drop. In this case, you're aiming to drop the column labeled 'job'.

### `axis=1`

The `axis` parameter decides whether you want to drop a row or a column:
- `axis=0`: This is the default and refers to rows. 
- `axis=1`: Refers to columns. Here, since `axis=1`, you're indicating that you want to drop a column, not a row.

### `inplace=True`

- By default, operations in `pandas` return a new DataFrame and leave the original untouched.
- If `inplace=True`, it means the DataFrame will be modified in place and nothing will be returned. The original DataFrame (`df` in this case) will be changed without creating a new object.
  
In summary, this line of code is deleting the column named 'job' from the DataFrame `df` without returning a new DataFrame (i.e., modifying `df` directly).






=========================================================================
Exporting to CSV and Excel - along with their parameters
=========================================================================
To export a DataFrame to a CSV or Excel file in pandas, you can use the `to_csv()` and `to_excel()` methods, respectively.

### 1. Exporting to CSV:
```python
df.to_csv('filename.csv')
```

### Common Parameters for `to_csv()`:
- **path_or_buf**: The file path or object to save the DataFrame. If not provided, it returns the resulting CSV format as a string.
- **sep**: Delimiter to use. Default is ',' for CSV.
- **na_rep**: String representation of NaN to use. Default is an empty string.
- **float_format**: Format string for floating point numbers.
- **columns**: Columns to write. If not provided, writes all columns.
- **header**: Whether to write the column headers. Default is True.
- **index**: Whether to write the row names (index). Default is True.
- **date_format**: Format string for datetime objects.

### 2. Exporting to Excel:
First, you'll need to install the `openpyxl` package to write to Excel files:
```
pip install openpyxl
```

Then, you can use the following command to save your DataFrame to an Excel file:
```python
df.to_excel('filename.xlsx')
```

### Common Parameters for `to_excel()`:
- **excel_writer**: Path or ExcelWriter object.
- **sheet_name**: Name of the sheet in the Excel file.
- **na_rep**: Representation for NaN values. Default is an empty string.
- **float_format**: Format string for floating point numbers.
- **columns**: Columns to write. If not provided, writes all columns.
- **header**: Whether to write the column headers. Default is True.
- **index**: Whether to write the row names (index). Default is True.
- **startrow**: Upper left cell row to dump data frame.
- **startcol**: Upper left cell column to dump data frame.
- **engine**: Write engine to use – `openpyxl` is the default.

Remember, when saving data, especially to CSV, you might encounter encoding issues, so sometimes it's a good idea to explicitly specify the encoding. If you're not sure which encoding to use, 'utf-8' is a safe bet.





=========================================================================
Normalization and Standardization
=========================================================================
Normalization and standardization are techniques used to preprocess data, especially in the context of machine learning. They transform the data to fit within a specific scale, like 0-1, or to have a mean of 0 and a standard deviation of 1. 

### Normalization:
Normalization typically means rescaling features to lie between a given minimum and maximum value, typically between zero and one. The most common formula for normalization is:
\[ \text{Normalized Value} = \frac{\text{Value} - \text{Min}}{\text{Max} - \text{Min}} \]

#### Real-life example:
Imagine you're working on predicting house prices and you have features like the size of the house (in square feet) and the number of bedrooms. The size of the house may range from 500 to 5000 sq.ft, while the number of bedrooms may range from 1 to 5. Because these features are on different scales, normalizing them can help certain algorithms perform better.

### Standardization:
Standardization, on the other hand, transforms the data to have zero mean and a standard deviation of one. It can be computed with:
\[ \text{Standardized Value} = \frac{\text{Value} - \text{Mean}}{\text{Standard Deviation}} \]

#### Real-life example:
Suppose you're comparing the test scores of students from different schools. One school might have a grading system of 0-100, while another has a system of 0-10. To compare the scores of students across these schools, you might standardize the scores.

### Python example using Pandas:

Given a DataFrame `df` with a column 'A', here's how you can normalize and standardize:

```python
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50]
})

# Normalize column 'A'
df['A_normalized'] = (df['A'] - df['A'].min()) / (df['A'].max() - df['A'].min())

# Standardize column 'A'
df['A_standardized'] = (df['A'] - df['A'].mean()) / df['A'].std()

print(df)
```

### When to use them:

1. **Algorithms sensitive to feature scales**: Algorithms like gradient descent, k-means clustering, or k-nearest neighbors, which are sensitive to the scales of features, will benefit from normalization or standardization.
  
2. **Regularization**: If you're using regularization in linear regression or logistic regression, it's good to standardize the features so that the penalization term treats all features equally.

3. **PCA**: Principal Component Analysis assumes that the features have been centered around zero. So, it's a good practice to standardize the features before using PCA.

Remember that not all algorithms require normalization or standardization. Trees-based algorithms like decision trees or random forests are scale-invariant, meaning they perform the same regardless of the scale of features.


    ================================================================================
    WHEN TO USE EACH
    ================================================================================
    Both normalization and standardization are techniques to re-scale features, but their use depends on the specific context and the type of data at hand. Let's understand the differences between the two and the scenarios in which each might be preferable.

    ### Normalization:
    Normalization scales the data between a specified range (usually 0 to 1). The formula for normalization is:
    \[ \text{Normalized Value} = \frac{\text{Value} - \text{Min}}{\text{Max} - \text{Min}} \]

    #### When to Use Normalization:
    1. **Data with Undefined Boundaries**: When your data doesn't have a clear or known distribution, normalization can be a good choice. 
    2. **Neural Networks**: Neural networks often require their input data to be on a scale of 0 to 1. This is especially true for the input neurons. 
    3. **Algorithms that Use Distance Metrics**: Algorithms like KNN and K-Means clustering which use distance measures can be sensitive to the magnitude of data. Normalizing ensures that each feature contributes approximately proportionately to the final distance.
    4. **Image Data**: For image data, pixel values typically range from 0 to 255. By normalizing, you rescale these values to the range 0 to 1.

    ### Standardization:
    Standardization centers the data around zero and scales it in terms of standard deviation. The resulting data has a mean of 0 and a standard deviation of 1. The formula for standardization is:
    \[ \text{Standardized Value} = \frac{\text{Value} - \text{Mean}}{\text{Standard Deviation}} \]

    #### When to Use Standardization:
    1. **Assumptions about Data's Distribution**: Many algorithms, like linear regression (when using regularization), SVM, or logistic regression, make implicit assumptions about the data being normally distributed. Standardization can help in such cases.
    2. **PCA**: Principal Component Analysis is affected by the scales of the features; hence, it's a standard practice to standardize the data before using PCA.
    3. **Regularization**: Regularization techniques in linear regression or logistic regression are sensitive to the scale of data. Standardizing helps ensure that all features are treated equally in the regularization term.
    4. **Algorithms with Weight Updates**: Algorithms like gradient descent adjust weights based on the gradient of the error with respect to the feature. Features with larger scales can unduly influence the weight updates. Standardization mitigates this.
    5. **Comparing Features**: If you want to compare the coefficients of a linear regression model, standardizing can help in determining which features have more predictive power.

    ### In Summary:
    1. If you're unsure about the distribution of your data or you know it's not Gaussian, and you need values to be between 0 and 1, use normalization.
    2. If your algorithm makes assumptions about your data having a Gaussian distribution, and it does not require a bounded range, use standardization.
    3. If you're combining data sources that have different scales or units, consider standardizing.

    Finally, it's always good to test both normalization and standardization to determine which approach yields better performance for your specific use case.


        ================================================================================
        Gaussian Distribution
        ================================================================================
        The Gaussian distribution, also known as the normal distribution, is a continuous probability distribution characterized by a symmetrical bell-shaped curve. It is one of the most important and widely used distributions in statistics and natural sciences.

        #### Properties:
        1. **Symmetry**: The curve is symmetrical around its mean.
        2. **Mean, Median, Mode**: All are equal and located at the center of the distribution.
        3. **Parameters**: The Gaussian distribution is defined by two parameters: the mean (\( \mu \)) and the standard deviation (\( \sigma \)).
        4. **Bell Shape**: It has a bell-shaped density curve.
        5. **Inflection Points**: The distribution has inflection points at \( \mu \pm \sigma \).

        #### Mathematical Expression:
        The probability density function (pdf) of the Gaussian distribution is given by:
        \[ f(x | \mu, \sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]
        Where:
        - \( x \) is a variable.
        - \( \mu \) is the mean of the distribution.
        - \( \sigma \) is the standard deviation.
        - \( \sigma^2 \) is the variance.

        #### Importance & Applications:
        1. **Central Limit Theorem (CLT)**: One of the reasons the normal distribution is so prevalent in statistics is the CLT, which states that, under certain conditions, the sum of a large number of random variables will be approximately normally distributed, regardless of their individual distributions.
        2. **Statistics & Machine Learning**: Many statistical methods and machine learning algorithms make underlying assumptions related to the normal distribution of data or errors.
        3. **Natural Phenomena**: Many natural phenomena, like height, blood pressure, or IQ scores, follow a near-normal distribution.
        4. **Quality Control**: In manufacturing and business, the normal distribution can be used for quality control and understanding variations.
        5. **Finance**: Stock returns and other financial instruments are often analyzed using tools that assume a normal distribution (though this assumption can be problematic with "fat-tailed" real-world financial data).

        #### Limitations:
        While the Gaussian distribution is incredibly useful, it's essential to recognize that not all data is normally distributed. In some cases, data might have heavy tails (more frequent large outliers) or might be skewed. Assumptions of normality need to be checked, especially in statistical modeling, to ensure that conclusions and predictions are valid.







=========================================================================
Generalized Meaning
=========================================================================
In the context of the explanation about Pandas' Series being a "generalized NumPy array," the term "generalized" means that the Series object extends or broadens the concept of a NumPy array by adding more functionality and flexibility.

A NumPy array is a homogeneous n-dimensional array, meaning that all elements must be of the same type. It uses integer indices to access the elements.

On the other hand, a Pandas Series, while still being a one-dimensional array, can have labels (indices) of any hashable type, not just integers, and can contain mixed data types. This makes it more versatile and adaptable to different use cases.

In this sense, the Pandas Series is a more general or broadened version of a NumPy array, capable of handling a wider variety of scenarios and data structures. That's what "generalized" refers to in this context.





