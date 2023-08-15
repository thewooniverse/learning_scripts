# Documentation: 
https://pandas.pydata.org/docs/user_guide/index.html#user-guide

https://pandas.pydata.org/docs/user_guide/indexing.html#indexing << indexing data






# Notes and exercises from:
https://www.youtube.com/watch?v=iGFdh6_FePU&t=627s

### Notes ###
Series is like a column of data, and a dataframe is much like a spreadsheet.
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. 
Like Series, DataFrame accepts many different kinds of input:

#### Practice questions (in practices_2.py): ####
0. Load from the London weather series and play around with the indexes
1. Create a new series with random numbers
1.a. Play around with Series - indexing and slicing.

2. Create a new dataframe with random numbers
2.a.







PRACTICE ALL OF THE BELOW METHODS

Indexing and slicing are fundamental operations in pandas for selecting and manipulating data. There are several ways to index and slice a DataFrame:

1. **By Columns**:
   - Using column labels:
     ```python
     df['ColumnName']
     ```

   - Using multiple columns:
     ```python
     df[['Column1', 'Column2']]
     ```

2. **By Rows** using `loc` and `iloc`:
   - `loc` is primarily label based indexing:
     ```python
     df.loc[row_label]
     df.loc[row_start:row_end]
     ```

   - `iloc` is primarily integer based indexing:
     ```python
     df.iloc[row_index]
     df.iloc[start_index:end_index]
     ```

3. **By Rows and Columns**:
   - Using `loc`:
     ```python
     df.loc[row_label, 'ColumnName']
     df.loc[row_start:row_end, ['Column1', 'Column2']]
     ```

   - Using `iloc`:
     ```python
     df.iloc[row_index, column_index]
     df.iloc[start_index:end_index, start_column:end_column]
     ```

4. **Boolean Indexing**:
   - Based on condition:
     ```python
     df[df['ColumnName'] > value]
     ```

   - Multiple conditions:
     ```python
     df[(df['Column1'] > value1) & (df['Column2'] < value2)]
     ```

5. **Using `isin` for Filtering**:
   - Filtering based on list of values:
     ```python
     df[df['ColumnName'].isin([value1, value2])]
     ```

6. **Using the `query` Method**:
   - Useful for complex conditions:
     ```python
     df.query("Column1 > value1 & Column2 < value2")
     ```

7. **Using `xs` for Cross Section**:
   - Selecting data at a particular level of a MultiIndex DataFrame:
     ```python
     df.xs(key=value, level='LevelName')
     ```

8. **Using `at` and `iat` for Faster Access**:
   - `at` allows fast access to a single value using row and column labels:
     ```python
     df.at[row_label, 'ColumnName']
     ```

   - `iat` allows fast access to a single value using row and column integer-positions:
     ```python
     df.iat[row_index, column_index]
     ```

9. **Slicing with `head` and `tail`**:
   - Get the first `n` rows:
     ```python
     df.head(n)
     ```

   - Get the last `n` rows:
     ```python
     df.tail(n)
     ```

These are just the basic ways to index and slice data in a pandas DataFrame. As you work with pandas, you'll find that it provides an extensive set of tools and methods to facilitate a wide range of data selection and manipulation tasks.

