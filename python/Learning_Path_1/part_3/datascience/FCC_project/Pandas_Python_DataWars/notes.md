LINK TO PROJECT:
https://www.youtube.com/watch?v=gtjxAH8uaP0&t=1891s
https://www.datawars.io/articles/pandas-data-science-by-example-freecodecamp-video-series

NOTE:
All projects will have their own link and saved on the cloud, its a good platform to practice stuff in.
Notes saved here natively will just be to copy and organize notes.


# 1 - DataFrames practice: working with English Words

## df['column'].value_counts() METHOD
If you want to count occurrences of each unique value in a specific column of a pandas DataFrame, you can use the `value_counts()` method. 

```python
import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Mike', 'Anna', 'Mike', 'John', 'John'],
    'Age': [23, 25, 23, 25, 24, 23, 26]
}
# If you want to count occurrences of each unique value in the 'Name' column, you can do:
df = pd.DataFrame(data)
name_counts = df['Name'].value_counts()
print(name_counts)
# The result is a Series where the index consists of the unique values from the 'Name' column, and the corresponding values are the counts of these unique values.
Output:
John    3
Anna    2
Mike    2
Name: Name, dtype: int64
```

booleans are &~|




# 2 - Querying and Filtering Pokemon data

```python
# Multi conditional locating / filtering 
df_first_3_gen = df.loc[
    ((df['Generation'] == 1)
    |
    (df['Generation'] == 2)
    |
    (df['Generation'] == 3))
    &
    (df['Type 1'] == 'Water')
]

df_dragons_in_last2gens = df.loc[
    (
        (df['Type 1'] == 'Dragon')
        |
        (df['Type 2'] == 'Dragon'))
    &
    (
        (df['Generation'] == df['Generation'].max())
        |
        (df['Generation'] == df['Generation'].max()-1)
    )
    
]
df_dragons_in_last2gens.sort_values(by='Total', ascending=False) # finds the strongest dragons in last 2 gen
```

```python
# getting top 5% and bottom 5% outlier pokemons using conditional statements and quantiles;
# qunatiles provide me with what number for that column defines the quantile / marks; so df['speed'].quantile(.05) gave me the lowest 5%
slow_fast_df = df.loc[
    (df['Speed'] < df['Speed'].quantile(.05))
    |
    (df['Speed'] > df['Speed'].quantile(.95))
]
```










# 3 - Birthdady Paradox in NBA teams.
```python
def nCr(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n-k))

def birthday_probability(number_of_people):
    return 1 - ((364/365) ** nCr(number_of_people, 2))

teams = df['Team'].unique() # unique gives me a array of the unique instances
teams = list(teams)

for team in teams:
    team_df = df.loc[df['Team'] == team]
    team_player_comb = pd.DataFrame(combinations(team_df['Player'], 2), columns = ['Player 1', 'Player 2'])
    team_bday_comb = pd.DataFrame(combinations(team_df['Birthday'], 2), columns = ['Birthday 1', 'Birthday 2'])
    team_full_comb = pd.concat([team_player_comb, team_bday_comb], axis=1)
#     print(team_full_comb)
    matching_bdays = team_full_comb.loc[team_full_comb['Birthday 1'] == team_full_comb['Birthday 2']]
    if len(matching_bdays) != 0:
        print(f'Matching players in {team}, there were {len(team_df)} players in the team.')
        print(f"This means, that there were {round(birthday_probability(len(team_df)), 2) * 100}% of two people having the same birthday.\n")
        print(matching_bdays)
        print("\n\n")


```







# 4 - Matching Strings by Similarity using Levenshtein distance
```python
list(df1['CLIENT'].values) # similar to the previous exercises' df['Team].unique(), we can also access the values to attain the list of values


df = pd.DataFrame(
    itertools.product(df1['CLIENT'].values, df2['Firm Name'].values),
    columns=['CSV 1', 'CSV 2']
)
# this example basically uses itertools.product to create a dataframe
```


## Using Apply on single and multiple columns
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4]})

# Function to square a number
def square(x):
    return x ** 2

# Create new column 'B' as square of 'A'
df['B'] = df['A'].apply(square)
print(df)

# Create DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Function to add two numbers
def add_columns(row):
    return row['A'] + row['B']

# Create new column 'C' as sum of 'A' and 'B'
df['C'] = df.apply(add_columns, axis=1)

print(df)
```


```Python - example in exercise
def calc_ratio(row):
    return fuzz.partial_ratio(row['CSV 1'], row['CSV 2'])

# df['Ratio Score'] = df.apply(calc_ratio, axis=1)

#  another approach
score = [fuzz.partial_ratio(c1,c2) for c1,c2 in df[['CSV 1', 'CSV 2']].values]
df['Ratio Score 2'] = score
```





# 4 - Cleaning Google Playstore data
## changing / manipulating whole dataframes vs. algorithimically looping
- Its often better to use location and string manipulations like the examples in this exercise rather than looping through the dataframe.
- Keep working with strings until you're sure you want to change it into another value -> essential step of the cleaning process.

## getting the columns that are missing values;
df.isna().sum()



## cleaning the Rating column from values that are too high (above> 5):

```Python 
df.loc[df['Rating'] > 5, 'Rating'] = np.nan
```

- `df['Rating'] > 5`: This part creates a boolean mask, where each element will be `True` if the corresponding element in the column `'Rating'` is greater than 5, and `False` otherwise.

- `df.loc[...]`: The `.loc` accessor is used for label-based indexing of the DataFrame. In this case, it is used to select rows that satisfy the condition specified by the boolean mask (`df['Rating'] > 5`).

- `, 'Rating'`: This part indicates that we are only interested in updating the `'Rating'` column of the DataFrame.

- `= np.nan`: Finally, this part assigns `NaN` (Not a Number, from the NumPy library denoted as `np.nan`) to the selected elements.

So, to summarize: The code will look for all rows where the value in the `'Rating'` column is greater than 5. For those rows, it will replace the value in the `'Rating'` column with `NaN`, effectively marking them as missing or invalid values.






## Cleaning the Reviews section for 6M -> 6_000_000 transformations;
```Python 
df.loc[df['Reviews'].str.contains('M'), 'Reviews']
# ^this only gets the 'Reivews' column as a result, returns a series / locates just the series of the column 'Reviews' in the dataframe the contains 'M'

(pd.to_numeric(df.loc[df['Reviews'].str.contains('M'), 'Reviews'].str.replace('M', "")) * 1_000_000).astype(str)
# this transforms the above series, first replacing "M" -> '', then transforming it into a numeric type and multiplying it by a million, then transforming it back into str

df.loc[df['Reviews'].str.contains('M'), 'Reviews'] = (pd.to_numeric(df.loc[df['Reviews'].str.contains('M'), 'Reviews'].str.replace('M', "")) * 1_000_000).astype(str)
# this code snippet reassigns those specific rows where 'M' is found in the original dataframe, into the newly transformed series.
# targets and replaces the values.

df.loc[df['Reviews'].str.contains('M'), 'Reviews']
# this returns an empty series of 'Reviews' as there are no longer rows containing the string 'M'.

df['Reviews'] = pd.to_numeric(df['Reviews'])
# this transforms the whole column into a numeric;

## this section was really important in learning the concepts of cleaning, targeting and the re-assigning values.

```



## Targeting duplicates in "Apps" Column

```python

# 4. How many duplicated apps are there?
df.duplicated(subset=['App']) # returns a boolean index 


df.loc[df.duplicated(subset=['App'], keep=False)].sort_values(by='App').head(10)
# ^by default; this method shows the second duplicated value, instead of the first instance;
# as it considers the first the "real one"
# e.g.
# Twitter
# Twitter <-
# Twitter <- only these two, after first (default is keep=first) are selected as dupes
# the keep=False parameter, marks all instances incl first instance as True
# keep=False parameter marks all duplicates as True incl first / last one.
# then running .shape on the above gives the number of entries





# 5. Drop duplicated apps keeping the ones with the greatest number of reviews
org_df = df.loc[df.duplicated(subset='App',  keep="last")].sort_values(by=['App', 'Reviews'])
org_df.drop_duplicates(subset='App', keep='last')
# testing with a test df called org_df, and seeing that it works. (alternate is to create a df copy so that I can copy() it back if I mess up as a save point)

df.sort_values(by=['App', 'Reviews'], inplace=True) # we just sort the dataframe in place here again
df.drop_duplicates(subset='App', keep='last', inplace=True) # then we drop the duplicates and keep the last (whereas, in sorting our ascending was True by default) so the final entry which has the highest amount of reviews goes last.

# the longer way would have been to just use the drop duplicates to drop the rows as well.




# 6. Format the Category column
# As 1.9 is a wrong category, we transform it into "Unknown" category
df.loc[df['Category'] == "1.9", 'Category'] = 'Unknown'

# Replace underscores with whitespaces
df["Category"] = df['Category'].str.replace('_', ' ')

# Capitalize the column
df['Category'] = df['Category'].str.capitalize()


# 8. Clean and convert the Size column to numeric (representing bytes)
df_copy8 = df.copy()
df['Size']
# locate all of the columns that contain a k

# # target and modify those columns
# ## first, remove all of the 'k', and convert it into a numeric type, multiply it by 1024 
kbyte_series = df.loc[df['Size'].str.contains("k")]['Size'].str.replace('k', '')
kbyte_series = pd.to_numeric(kbyte_series)
kbyte_series = (kbyte_series * 1024).astype(str)

df.loc[df['Size'].str.contains("k"), 'Size'] = kbyte_series

# # do the same process for mbytes
mbyte_series = df.loc[df['Size'].str.contains("M")]['Size'].str.replace('M', '')
mbyte_series = pd.to_numeric(mbyte_series)
mbyte_series = (mbyte_series * 1024 * 1024).astype(str)
mbyte_series # correct megabytes in strings, now reassigning

df.loc[df['Size'].str.contains("M"), 'Size'] = mbyte_series

# to_numeric() the whole column, and then fill the NaN coerced in transition to 0
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')
df['Size'] = df['Size'].fillna(0)


##### 9. Clean and convert the `Price` column to numeric
# first of all, remove all of the $ signs
df['Price'] = df['Price'].str.replace('$', '')
df['Price']

# then change all of the Free -> 0
df.loc[df['Price'] == 'Free', 'Price'] = 0

# then change the table to numeric
df['Price'] = pd.to_numeric(df['Price'])



##### 10. Paid or Free?
# Create a new column where default = Free
df['Distribution'] = 'Free'

# target the rows where price != 0, and set it to 'Paid'
df.loc[df['Price'] > 0, 'Distribution'] = 'Paid'



## 14/15 - most expensive and popular game / finance app
games_df = df.loc[df['Category'] == 'Game']
max_game_price = games_df['Price'].max()
games_df.loc[games_df['Price'] == max_game_price]

finance_df = df.loc[df['Category'] == 'Finance']
finance_df = finance_df.sort_values(by='Installs', ascending=False)
finance_df
# this is another way to find an answer, the above method goes for matching with max value
# this approach simply sorts and displays, so you can see which row has the highest installs.


df_free_games = df.loc[
    (df['Distribution'] == "Free")
    &
    (df['Category'] == 'Game')
]
df_free_games.sort_values(by='Reviews', ascending=False)
# same approach but with more complex selection




# get the most popular lifestyle app
lifestyle_apps = df.loc[df['Category'] == 'Lifestyle']
most_popular_lifestyle_app = lifestyle_apps.loc[
    lifestyle_apps['Installs'] == lifestyle_apps['Installs'].max()
]
most_popular_lifestyle_app

# most_popular_lifestyle_app.iloc[0, 'Installs']
# calculate, with the row data the "data transferred = installs x size", then calculate TBs
installs_value = most_popular_lifestyle_app['Installs'].iloc[0]
size_value = most_popular_lifestyle_app['Size'].iloc[0]

byte_size = (installs_value * size_value)
tb = (byte_size)/1024**4



# df_copy_test = df.copy()
df['Data Transferred TB'] = round((df['Installs'] * df['Size'])/1024**4, 1)
df['Data Transferred TB']
df.loc[df['App'] == 'Tinder'] # double checked value

```



















```Python 
df.loc[df['Reviews'].str.contains('M')]
# returns a dataframe with rows
df.loc[df['Reviews'].str.contains('M'), 'Reviews']
# returns simply a series with rows and the value of the column 'Reviews'
df.loc[df['Reviews'].str.contains('M'), 'Reviews'].str.replace('M', '')
# this returns a dataframe that now has replaced the rows that has M in the reviews (to stand for millions) with '', now the data is ready for transformation

pd.to_numeric(df.loc[df['Reviews'].str.contains('M'), 'Reviews'].str.replace('M', '')) 
```













============================================================================================================
# df.duplicated method;
============================================================================================================

The `df.duplicated()` method in pandas is used to identify duplicate rows in a DataFrame based on specified columns. It returns a Boolean Series where a `True` or `False` value indicates whether a row is a duplicate.

### Parameters:

- **subset**: Columns to consider when identifying duplicates. By default, it uses all columns.
- **keep**: Controls which duplicates to mark.
  - `'first'` (default): Marks duplicates as `True` except for the first occurrence.
  - `'last'`: Marks duplicates as `True` except for the last occurrence.
  - `False`: Marks all duplicates as `True`.

### Return:

- A Boolean Series that has the same index as the original DataFrame.

### Core Concepts:

- **DataFrame**: The primary pandas data structure, similar to a table in a database, an Excel worksheet, or a data frame in R.
- **Boolean Series**: A Series of `True` and `False` values, typically used for conditional filtering.
- **Index**: The unique identifier for each row in a DataFrame.

### Real-world Example:

Consider you have a dataset of customer transactions and you want to find out the duplicated entries.

```python
import pandas as pd

# Sample DataFrame
data = {'CustomerID': [1, 2, 2, 3, 4, 4],
        'Transaction': [50, 30, 30, 40, 60, 60]}

df = pd.DataFrame(data)

# Using df.duplicated to find duplicate rows
duplicates = df.duplicated(subset=['CustomerID', 'Transaction'], keep='first')
print("Duplicate Rows except the first occurrence:")
print(df[duplicates])
```

Output:

```
Duplicate Rows except the first occurrence:
   CustomerID  Transaction
2           2           30
5           4           60
```

In this example:

- The DataFrame `df` is created with sample data.
- The `duplicated()` method checks for duplicates using all columns since the `subset` parameter is not specified. The `keep='first'` parameter ensures that only the duplicates after the first occurrence are marked as `True`.
- The resulting Boolean Series `duplicates` is used to filter the DataFrame and output the duplicate rows.

### Best Practices:

1. Be specific with the `subset` parameter if you only need to consider certain columns for finding duplicates.
2. Use `keep=False` if you want to mark all duplicates, including the first occurrence, which is useful when you want to completely eliminate duplicates from the dataset.

This should give you a comprehensive understanding of the `df.duplicated()` method in pandas.