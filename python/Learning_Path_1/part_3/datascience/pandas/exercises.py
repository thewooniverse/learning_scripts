import datetime
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Exercises as described in exercises.md in the same directory - one of the more comprehensive / notes and practices with examples


"""
### Exercise 1: Reading and Inspecting Data
- Read a CSV file into a Pandas DataFrame.
- Display the first 5 rows.
- Display the last 5 rows.
- Print the summary statistics using the `describe` method.
- Find the number of missing values in each column.
"""
df = pd.read_csv(f'{os.getcwd()}{os.path.sep}london_weather.csv')
print(df.head())
print(df.tail())
print(df.describe())

missing_values = df.isna()
print(missing_values.sum())
"""
df.isna() itself returns a boolean same sized object if values are Na (None or np.NaN)

date                   0
cloud_cover           19
sunshine               0
global_radiation      19
max_temp               6
mean_temp             36
min_temp               2
precipitation          6
pressure               4
snow_depth          1441
dtype: int64
"""



"""
### Exercise 2: Filtering and Sorting
- Filter the rows based on a specific condition.
- Sort the DataFrame based on one or more columns.
- Select specific columns to create a new DataFrame.
"""
hotter_than_average_days = df[df['mean_temp'] > df['mean_temp'].mean()]
print(hotter_than_average_days) # returns 7582 rows

df_sorted_maxtemp = df.sort_values(by='max_temp', ascending=False) # default is ascending, so to make it descending we must do ascending=False
print(df_sorted_maxtemp)
df_sorted_mintemp = df.sort_values(by='min_temp') # ascending by default, this is good for sorting the coldest day first
print(df_sorted_mintemp)

temperature_only_df = df[['date', 'max_temp', 'min_temp', 'mean_temp']]
print(temperature_only_df)

df_sorted_min_precipitation = df.sort_values(by='precipitation', ascending=False)
print(df_sorted_min_precipitation)


"""
### Exercise 3: Grouping and Aggregation
- Group the DataFrame by a specific column (e.g., a category).
- Calculate the mean or sum for each group.
- Create a pivot table.
"""
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.set_index('date', inplace=True)
monthly_mean = df.resample('M').mean()
monthly_sum = df.resample('M').max()
# print(monthly_sum)

pivot_table = df.pivot_table(values='precipitation', index='cloud_cover', columns='sunshine', aggfunc='mean')
# print(pivot_table)







"""
### Exercise 4: Merging and Joining
- Create two DataFrames and merge them using different types of joins (inner, outer, left, right).
- Concatenate two DataFrames vertically and horizontally.
"""
df_2 = pd.DataFrame({
    "name" : pd.Series(['john', 'jake', 'jimmy', 'jackson', 'jack', 'jhon']),
    "savings" : pd.Series([50, 35, 1.5, 400, 50, 20]),
    'salary': pd.Series([120, 150, 200, 500, 60, 75])
})

df_3 = pd.DataFrame({
    "name" : pd.Series(['becky', 'susan', 'manny', 'jin', 'john', 'jake', 'becky']),
    "salary": pd.Series([250, 100, 300, 40]),
    'gender': pd.Series(["female", 'female', 'male', 'male'])
})

concat_df = pd.concat([df_2, df_3])
print(concat_df)
"""
      name  savings  salary  gender
0     john     50.0   120.0     NaN
1     jake     35.0   150.0     NaN
2    jimmy      1.5   200.0     NaN
3  jackson    400.0   500.0     NaN
4     jack     50.0    60.0     NaN
5     jhon     20.0    75.0     NaN
0    becky      NaN   250.0  female
1    susan      NaN   100.0  female
2    manny      NaN   300.0    male
3      jin      NaN    40.0    male
4     john      NaN     NaN     NaN
5     jake      NaN     NaN     NaN
6    becky      NaN     NaN     NaN

as we can see it jsut stacks dataframes vertically.
"""


inner_joined_df = pd.merge(df_2, df_3, on='name')
print(inner_joined_df)
outer_joined_df = pd.merge(df_2, df_3, on='name', how='outer')
print(outer_joined_df)

"""
INNER OUTPUT:

   name  savings  salary_x  salary_y gender
0  john     50.0       120       NaN    NaN
1  jake     35.0       150       NaN    NaN

OUTER OUTPUT (without on='name')
       name  savings  salary  gender
0      john     50.0   120.0     NaN
1      jake     35.0   150.0     NaN
2     jimmy      1.5   200.0     NaN
3   jackson    400.0   500.0     NaN
4      jack     50.0    60.0     NaN
5      jhon     20.0    75.0     NaN
6     becky      NaN   250.0  female
7     susan      NaN   100.0  female
8     manny      NaN   300.0    male
9       jin      NaN    40.0    male
10     john      NaN     NaN     NaN
11     jake      NaN     NaN     NaN
12    becky      NaN     NaN     NaN

OUTER OUTPUT (with on='name')
       name  savings  salary_x  salary_y  gender
0      john     50.0     120.0       NaN     NaN
1      jake     35.0     150.0       NaN     NaN
2     jimmy      1.5     200.0       NaN     NaN
3   jackson    400.0     500.0       NaN     NaN
4      jack     50.0      60.0       NaN     NaN
5      jhon     20.0      75.0       NaN     NaN
6     becky      NaN       NaN     250.0  female
7     becky      NaN       NaN       NaN     NaN
8     susan      NaN       NaN     100.0  female
9     manny      NaN       NaN     300.0    male
10      jin      NaN       NaN      40.0    male

"""

"""
GPT notes on the section (joining, merging, concatenating)
If you're looking to stack dataframes vertically, use concat() or append().
For SQL-like JOIN operations, merge() is the most suitable.
If you want to join on indices, join() is the best choice.

concat()
- stacks dataframes vertically or horizontally
- used when you have dataframes of similar columns or rows and you want to concatenate them.
"""
# Concatenating example by GPT
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df1, df2])
# print(result)
"""
   A  B
0  1  3
1  2  4
0  5  7
1  6  8
"""


"""
merge()
- used to merge dataframes using simialr columns, simialr to SQL JOIN operations.
- used when you ahve two dataframes with one or more common columns, and you want to merge them based on thsoe columns.

Types of merge:
Inner: Use the intersection of keys from both dataframes.
Outer: Use the union of keys from both dataframes.
Left: Use keys from the left dataframe only.
Right: Use keys from the right dataframe only.

The default type is param: how=inner.
"""
customers = pd.DataFrame({'customer_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
orders = pd.DataFrame({'order_id': [101, 102, 103], 'customer_id': [1, 3, 3], 'product': ['Book', 'Toy', 'Pen']})
merged_df = customers.merge(orders, on='customer_id')
# print(merged_df)
merged_df = customers.merge(orders, on='customer_id', how='left')
# print(merged_df)
"""
Inner Join
   customer_id     name  order_id product
0            1    Alice       101    Book
1            3  Charlie       102     Toy
2            3  Charlie       103     Pen

Outer Join
   customer_id     name  order_id product
0            1    Alice     101.0    Book
1            2      Bob       NaN     NaN
2            3  Charlie     102.0     Toy
3            3  Charlie     103.0     Pen

In this example, left join == inner join result, and right join == outer join
"""















"""
### Exercise 5: Handling Missing Data
- Identify missing values in the DataFrame.
- Fill missing values using different strategies (mean, median, etc.).
- Drop rows or columns with missing values.
"""
# identifying missing vlaues
# print(df.isna()) # checking for entire dataframe
# print(df.isna().sum()) # check missing value for each column
# print(df.isna().sum().sum()) # 1533, total number of misisng values
# print(df['snow_depth'].isna().sum()) # 1441 - total number

# filling misisng values in different ways
filled_df = df.fillna(value=0) # inplace=True is also optional, but forth is I won't.
# print(filled_df.isna().sum()) # everything is filled, the new dataframe does not have any spots
ffilled_df = df.fillna(method='ffill')
bfilled_df = df.fillna(method='bfill')


# filling using mean, median, mode and interpolation
interpolated_df = df.interpolate(method='linear')
# print(interpolated_df.isna().sum()) # no missing values after

mean_fill_column = df['mean_temp'].fillna(df['mean_temp'].mean()) # we should do this in place, otherwise, the returned value would be the specific column that we filled.
# print(mean_fill_column) # returns specific column, but the fillna worked properly filling all NaN value with mean value.

mean_filled_df = df
mean_filled_df['mean_temp'].fillna(df['mean_temp'].mean(), inplace=True)
mean_filled_df['snow_depth'].fillna(df['snow_depth'].mean(), inplace=True)
# print(mean_filled_df.isna().sum()) # mean temp and snow depth now no longer has NaN values displayed

# dropping rows / columns with missing values
row_dropped_df = df.dropna()
column_dropped_df = df.dropna(axis=1)
# print(row_dropped_df.isna().sum())
# print(column_dropped_df.isna().sum()) # in this df the columns containing any NaN are dropped entirely.







"""
### Exercise 6: Date and Time Operations
- Create a date range using Pandas.
- Convert a string into a datetime object.
- Extract different components of a date (like year, month, day).
- Perform time-based indexing.

converting things to a datetime index for a dataframe unlocks a lot of handy features.
"""
monthly_dr = pd.date_range(start='2020-01-01', end='2020-12-31', freq='M')
print(monthly_dr)

monthly_df = pd.DataFrame(monthly_dr, columns=['date'])
monthly_df['r_numbers'] = pd.Series(np.random.randn(12))
monthly_df.set_index('date', inplace=True) # now that the DateTime index is set
print(monthly_df)

Q1 = monthly_df['2020-01-01' : '2020-04-01'] #ability to select data from specific timeframes
print(Q1)
"""
OUTPUT:
            r_numbers
date                 
2020-01-31  -0.275427
2020-02-29  -0.754436
2020-03-31  -0.693601
"""

# string <> datetime exercises
date_string = "21 June, 2021 15:30"
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y %H:%M")
# print(date_object) # 2021-06-21 15:30:00
day = date_object.day
# print(day) #21


# pd.to_datetime() - this is used for transforming a dataframe with a strign based date column into a datetime column.
data = {'date': ["21 June, 2021 15:30", "22 June, 2021 16:45", "23 June, 2021 14:20"]}
df_test = pd.DataFrame(data)
print(df_test)
df_test['date'] = pd.to_datetime(df_test['date'], format="%d %B, %Y %H:%M")
print(df_test)


"""
### Exercise 7: Data Visualization
- Create basic plots directly from Pandas (e.g., line plot, scatter plot, histogram).
- Use the Seaborn library to create more advanced plots (e.g., boxplot, heatmap).
"""
resampled_df = interpolated_df.resample('M').mean()
year_2020 = resampled_df['2020-01-01':'2020-12-31']
temperatures_monthly_2020 = year_2020[['mean_temp','max_temp','min_temp']]

print(temperatures_monthly_2020)
temperatures_monthly_2020.plot(kind='line')
plt.show()
sns.boxplot(data=temperatures_monthly_2020)
plt.show()











"""
### Exercise 8: Applying Functions
- Apply a custom function to a column using the `apply` method.
- Use `lambda` functions within `apply`.
"""

# using a custom function to calculate whether a month is hotter than average
def hotter_than_average(temperature, average_temp=temperatures_monthly_2020['mean_temp'].mean()):
    if temperature >= average_temp:
        return True
    else:
        return False
temperatures_monthly_2020['hotter_than_avg'] = temperatures_monthly_2020['mean_temp'].apply(hotter_than_average)
print(temperatures_monthly_2020)
"""
            mean_temp   max_temp   min_temp  hotter_than_avg
date                                                        
2020-01-31   7.554839   9.929032   5.235484            False
2020-02-29   8.156897  11.074138   5.320690            False
2020-03-31   8.030645  11.938710   4.174194            False
2020-04-30  12.353333  18.186667   6.573333            False
2020-05-31  15.187097  21.183871   9.248387             True
2020-06-30  17.535000  22.570000  12.580000             True
2020-07-31  18.633871  23.814516  13.535484             True
2020-08-31  20.606452  25.509677  15.738710             True
2020-09-30  16.616667  21.693333  11.580000             True
2020-10-31  11.922581  15.004839   9.038710            False
2020-11-30   9.806667  12.636667   7.026667            False
2020-12-31   6.232258   8.325806   4.187097            False
"""

mean_2020 = temperatures_monthly_2020['mean_temp'].mean()

# using a lambda function
temperatures_monthly_2020['max_temp_higher_than_yearly_mean'] = temperatures_monthly_2020['max_temp'].apply(lambda x: True if x > mean_2020 else False)
print(temperatures_monthly_2020)
"""
            mean_temp   max_temp   min_temp  hotter_than_avg  max_temp_higher_than_yearly_mean
date                                                                                          
2020-01-31   7.554839   9.929032   5.235484            False                             False
2020-02-29   8.156897  11.074138   5.320690            False                             False
2020-03-31   8.030645  11.938710   4.174194            False                             False
2020-04-30  12.353333  18.186667   6.573333            False                              True
2020-05-31  15.187097  21.183871   9.248387             True                              True
2020-06-30  17.535000  22.570000  12.580000             True                              True
2020-07-31  18.633871  23.814516  13.535484             True                              True
2020-08-31  20.606452  25.509677  15.738710             True                              True
2020-09-30  16.616667  21.693333  11.580000             True                              True
2020-10-31  11.922581  15.004839   9.038710            False                              True
2020-11-30   9.806667  12.636667   7.026667            False                             False
2020-12-31   6.232258   8.325806   4.187097            False                             False
"""

















"""
### Exercise 9: Data Transformation
- Normalize or standardize a numerical column.
- Convert a categorical column into dummy variables.
"""

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
"""
    A  A_normalized  A_standardized
0  10          0.00       -1.264911
1  20          0.25       -0.632456
2  30          0.50        0.000000
3  40          0.75        0.632456
4  50          1.00        1.264911
"""








"""
### Exercise 10: Saving Data
- Save a DataFrame to a CSV file.
- Save a DataFrame to an Excel file.
"""
# df.to_csv()
temperatures_monthly_2020.to_csv('temperatures_2020_london.csv')


# df.to_excel()
temperatures_monthly_2020.to_excel('temperatures_2020_london.xlsx', sheet_name='temperatures of 2020 London')






