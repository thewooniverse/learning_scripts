import numpy as np
import pandas as pd
import os

# This note is one of the good ones that were recently done.






# 0. Load from the London weather series and play around with the indexes
weather_df = pd.read_csv(f'{os.getcwd()}{os.path.sep}london_weather.csv')
# print(weather_df)


# 1. Create a new series with random numbers
# random_series = pd.Series(np.random.randn(10))
# print(random_series)

random_series = pd.Series(np.random.randn(10), index=['a','b','c','d','e','f','g','h','i','j'])
print(random_series) # prints another dataframe with same structure, but with the index as a-j

# simple slicing and indexing of series
# print(random_series[0]) # prints the first row, value  only
# print(random_series[:1]) # prints the first row, value and index
# print(random_series[:3]) # prints the first to third row (0,1,2) or in this case a,b,c
# print(random_series[[0,1,2,3]]) # prints rows a,b,c,d

# accessing elements based on index like a dictionary (or row name)
# print(random_series['c']) 
random_series['c'] = 13 # reassigns value of row c
# print(random_series) # value of c = 13

# slicing based on conditionals
# print(random_series[random_series>random_series.median()]) # prints the columns where the row value is bigger than the median value


# other slicing / targeting and indexing
# print(random_series.array) # prints the actual array backing the series





"""
Resetting the index for Series:
--
When applied to a Series, 
the method will return a DataFrame where the old index is turned into a column and the Series values form another column.
The resulting DataFrame will have a default integer-based index.
"""
s = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(s)
df_reset = s.reset_index()
print(df_reset)
"""
OUTPUT1:
a    1
b    2
c    3
d    4
dtype: int64

OUTPUT 2: index is moved to another column, default index is applied 
  index  0
0     a  1
1     b  2
2     c  3
3     d  4
"""





















# 2. Create a new dataframe with random numbers in different ways, with different data formats and ways of constructing!
# constructing DataFrames from Dict of Series or Dicts
data = {
    "age": pd.Series([50, 35, 95, 100, 69], index=['becky', 'susan', 'maccy', 'ronald', 'donald']),
    "gender": pd.Series(["female", "female", "female", "male", "male"], index=['becky', 'susan', 'ronald', 'millie', 'donald'])
}
df = pd.DataFrame(data) # index of the dataframe (each row is indexed by the name of the person)
df.index.name = "Names" # changes the name of the index column to Names
print(df)
"""
OUTPUT:
          age  gender
Names                  <<< names was added only after df.index.name = "Names" was executed
becky    50.0  female
donald   69.0    male
maccy    95.0     NaN
millie    NaN    male
ronald  100.0  female
susan    35.0  female

The assignments were all done without issue and the final table is a Union of the columns with missing values being assigned NaN
"""

df_2 = pd.DataFrame(data, index=['becky', 'susan', 'ronald', 'nancy'], columns=['age', 'location'])
print(df_2)
"""
OUTPUT:
          age location
becky    50.0      NaN
susan    35.0      NaN
ronald  100.0      NaN
nancy     NaN      NaN

The dataframe will only take the rows where the indexes and columns defined in the construction, once again filling empty datasets with NaN.
"""
print(df_2.columns)
print(df_2.index)
"""
columns = Index(['age', 'location'], dtype='object')
index = Index(['becky', 'susan', 'ronald', 'nancy'], dtype='object')
"""


"""
constructing from dict of ndarrays or lists
--
The ndarrays must all be the same length. If an index is passed, it must also be the same length as the arrays. 
If no index is passed, the result will be range(n), where n is the array length.
"""

data_2 = {
    "name": ['becky', 'susan', 'jimmy', 'carter'],
    "age": [10, 12, 15, 18],
    'height': [180, 130, 155, 180],
    'weight': [65, 45, 50, 100]
}

df_3 = pd.DataFrame(data_2)
print(df_3)
"""
OUTPUT:

     name  age  height  weight
0   becky   10     180      65
1   susan   12     130      45
2   jimmy   15     155      50
3  carter   18     180     100
"""
df_3.set_index('name', inplace=True) # usually, this would return a new list, but inplace=True makes it replace inplace

new_df = df_3.reset_index(drop=True)
print(new_df)


"""
Setting and Resetting the index for pandas DataFrames:
--
# setting the index
the index is a range(n) with n as the array length in the first table of df_3, 
however after I df_3.set_index() as above, it becomes this:

        age  height  weight
name                       
becky    10     180      65
susan    12     130      45
jimmy    15     155      50
carter   18     180     100


# resetting the index -> df.reset_index(drop=True)
--
This is particularly useful when the index of a DataFrame becomes messy or unordered, 
or when you simply want to revert an index to the default integer-based index after some operations.

drop=True parameter will drop and remove the old index.

new_df() above looks like this, where the old index "name" has been ddropped:

   age  height  weight
0   10     180      65
1   12     130      45
2   15     155      50
3   18     180     100


"""









"""
### selecting and manipulating columns ###
--
You can treat a DataFrame semantically like a dict of like-indexed Series objects. 
Getting, setting, and deleting columns works with the same syntax as the analogous dict operations:
"""

print(df_3['weight'])
"""
OUTPUT:
name
becky      65
susan      45
jimmy      50
carter    100
"""

# you can create new columns and run operations to create new columns as well
df_3['bmi'] = (df_3['weight'] / (df_3['height'] * 2)) * 100
df_3['overweight'] = df_3['bmi'] > 25
print(df_3)
"""
OUTPUT:
        age  height  weight        bmi  overweight
name                                              
becky    10     180      65  18.055556       False
susan    12     130      45  17.307692       False
jimmy    15     155      50  16.129032       False
carter   18     180     100  27.777778        True

By default, columns get inserted at the end. DataFrame.insert() inserts at a particular location in the columns:
"""

# deleting / popping columns like a dictionary
del df_3['overweight']
bmi = df_3.pop('bmi') # in this case, this is a series
print(df_3) # after both of these operations, df_3 no longer has the bmi and overweight columns


# changing the ordering of the columns
df_3 = df_3[['height', 'weight', 'age']]
print(df_3)
"""
OUTPUT: reordered dataframe

        height  weight  age
name                       
becky      180      65   10
susan      130      45   12
jimmy      155      50   15
carter     180     100   18
"""















"""
### INDEXING / SELECTION ###
More in depth covered here - https://pandas.pydata.org/docs/user_guide/indexing.html#indexing

--

                                       syntax    returns
operation                                               
select column                         df[col]     Series
select row by label             df.loc[label]     Series
select row by integer location   df.iloc[loc]     Series
slice rows                           df[5:10]  DataFrame
select rows by boolean vector    df[bool_vec]  DataFrame


loc:

It stands for label-based indexing.
You use it with labels/indices to select rows or columns.
It can accept boolean data to filter rows.
When slicing, both the start and stop of the range are included.
For example 

iloc:

It stands for integer-location based indexing.
You use it with integer-based positions to select rows or columns.
Doesn't consider the DataFrame's index or column labels for selection.
When slicing, it follows standard Python slicing rules where the start is inclusive and the stop is exclusive.

Basically ilocs are for like integer based stuff where you want to slice shit up using their location
Whereas location is more label based and conditional based
"""

# indexing using label based indexing
print(df_3.loc['susan']) # select rows simply by the index value
"""
OUTPUT:

height    130
weight     45
age        12
Name: susan, dtype: int64
"""

# loc[:] slicing based on index
print(df_3.loc['becky':'jimmy']) # << this would be useful for stuff like if index was time and we wanted to get rows of specific times
print(df_3.loc['susan':'becky']) # < does not output anything since the indexes are not valid / nothing in between
"""
       height  weight  age
name                      
becky     180      65   10
susan     130      45   12
jimmy     155      50   15

second statement outputs:
Empty DataFrame
Columns: [height, weight, age]
Index: []
"""


# indexing based on integer based indexing
print(df_3.iloc[0:2]) # prints the first two rows, 0,1 which is becky and susan


print(df_3[0:2]) # this also prints the first two rows, 0 and 1

"""
Both `df_3.iloc[0:2]` and `df_3[0:2]` will indeed yield the first two rows of the dataframe `df_3`. However, they are based on different underlying mechanics:

1. **`df_3.iloc[0:2]`**:
   - This uses `iloc`, which stands for integer-location based indexing. 
   It allows you to select rows (or columns) at particular positions in the dataframe using integer indices.
   - You explicitly specify that you want to select rows using integer indices.

2. **`df_3[0:2]`**:
   - This is a basic slicing technique using the DataFrame's default row indexer.
   - Pandas DataFrame directly supports slicing on rows without any additional method. 
   The syntax is similar to how you'd slice a Python list. This is essentially a shorthand for row slicing.

Despite them yielding the same result in this context, they operate on different principles. 
`iloc` is more general and can also be used for column indexing when you provide two arguments (one for row and one for column). 
On the other hand, the direct slicing (`df_3[0:2]`) is specifically for rows and cannot be used directly for columns. 

In practice, when you're working with rows, both methods will get the job done. 
But it's helpful to be aware of these nuances, especially when your tasks become more complex or when you want to be more explicit in your code.

TLDR --> iloc is used more for complex ones where we want to slice the whole dataframe rather than just rows
"""




"""
ROWS AND COLUMNS
"""
print(df_3.loc['becky':'susan', ['height', 'weight']]) # label based
print(df_3.iloc[0:3, 1:3]) # integer location based
"""
OUTPUT:
       height  weight
name                 
becky     180      65
susan     130      45

OUTPUT 2:
       weight  age
name              
becky      65   10
susan      45   12
jimmy      50   15
"""


"""
boolean based indexing
"""

# single condition
drinking_age = df_3[df_3['age'] > 15]
print(drinking_age)
print(df_3['age'] > 15) # < the conditional inside returns a boolean vector

"""
OUTPUT:
        height  weight  age
name                       
carter     180     100   18


OUTPUT2:

name
becky     False
susan     False
jimmy     False
carter     True
Name: age, dtype: bool
"""


# multiple conditions
## repopulating the two columns previously removed
df_3['bmi'] = (df_3['weight'] / (df_3['height'] * 2)) * 100
df_3['overweight'] = df_3['bmi'] > 25

overweight_and_legal_to_drink = (df_3['age'] > 15) & (df_3['bmi'] > 25)
print(overweight_and_legal_to_drink)
print(df_3[overweight_and_legal_to_drink]) # << using the boolean vector directly after constructing it
"""
OUTPUT 1:

name
becky     False
susan     False
jimmy     False
carter     True
dtype: bool



OUTPUT 2:

        height  weight  age        bmi  overweight
name                                              
carter     180     100   18  27.777778        True
"""





"""
Querying for complex conditions << not needed for now, master the above first boyyyyy
"""































# d = {
#     "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
#     "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])
# }
# df = pd.DataFrame(d)
# print(df.index)
# print(df.columns)





### Test snippets ###
# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)
# print(df)

# Setting 'A' as the index
df = df.set_index('A')
# print(df)
# Accessing using the index
# print(df.loc[1])  # Using .loc to access the row with index labeled 1

"""
The original data has a default index
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

When transformed such that A becomes the index...
   B  C
A      
1  4  7 <<<
2  5  8
3  6  9

Such that when we ask for df.loc[1], it returns the row values for B and C where the index value=1
B    4
C    7
"""
indexing_df = pd.DataFrame({
    "operation": ['select column', 'select row by label', 'select row by integer location', 'slice rows', 'select rows by boolean vector'],
    'syntax': ['df[col]', 'df.loc[label]', 'df.iloc[loc]', 'df[5:10]', 'df[bool_vec]'],
    "returns": ['Series', 'Series', 'Series', 'DataFrame', 'DataFrame']
})
indexing_df.set_index('operation', inplace=True)
# print(indexing_df)