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
## Premier League Match Analysis
============================================================================================================

```python
### Identify and clean invalid results in the result column

df.loc[df['home_goals'] > df['away_goals'], 'result'] = "H"
df.loc[df['away_goals'] > df['home_goals'], 'result'] = "A"
df.loc[df['home_goals'] == df['away_goals'], 'result'] = "D"
df['result'].value_counts()
# the important part here (and in many other areas) is to target the 'result' column only, after selecting the df.loc to set the values

# Calculate average goals per season
goals_per_season = df.groupby('season')['total_goals'].mean()
# groupby is an important one.


##### What's the team with most away wins?
results_series_by_team = df.groupby('away_team')['result'].value_counts().sort_values(ascending=False)
results_series_by_team

### Model Answer
df.groupby('away_team').apply(lambda rows: (rows['result'] == 'A').sum()).sort_values(ascending=False).head()


##### What's the team that received the least amount of goals while playing at home?
home_played_ratio = (df.groupby('home_team')['away_goals'].sum().sort_index()) / df.groupby('home_team')['home_team'].value_counts().sort_index()
home_played_ratio.sort_values(ascending=False)

### model answer
"""
We know the team is playing at home, so we need to group by home_team. Then, we can use the .size() method to get a count of how many games were played, and .sum() of away_goals (which are the goals that the home team received).
"""
away_goals_df = df.groupby('home_team')[['result', 'away_goals']].agg(
    {'result': 'size', 'away_goals': 'sum'}
).sort_values(
    by=['result', 'away_goals'], ascending=[False, True]
).rename(columns={'result': 'games_played', 'away_goals': 'goals_received'})

away_goals_df['ratio'] = away_goals_df['goals_received'] / away_goals_df['games_played']


##### What's the team with most goals scored playing as a visitor (away from home)?
df.groupby('away_team')['away_goals'].sum()
df.groupby('away_team')['away_team'].value_counts()
most_goals_as_away_team = (df.groupby('away_team')['away_goals'].sum()) / (df.groupby('away_team')['away_team'].value_counts())
most_goals_as_away_team.sort_values(ascending=False)

## model solution
away_goals_df = df.groupby('away_team')[['result', 'away_goals']].agg(
    {'result': 'size', 'away_goals': 'sum'}
).sort_values(
    by=['result', 'away_goals'], ascending=[False, False]
).rename(columns={'result': 'games_played', 'away_goals': 'goals_scored'})

away_goals_df['ratio'] = away_goals_df['goals_scored'] / away_goals_df['games_played']

```







============================================================================================================
## NBA 2017 Season Analysis
============================================================================================================



```python
##### 1. Merge `s2017_df` and `players_df` with a left join
df = s2017_df.merge(players_df, how='left', left_on='Player', right_on='name') 
# further notes on joining on the bottom section - however, its very intuitive / straight forward.


##### 4. Extract the names of the players that couldn't be matched
player_misses = list(df.loc[df['name'].isna(), 'Player'])
# gets the series of the column 'Player' where df['name].isna(), then transforms it into a list
player_misses
"""
OUTPUT:
['Luc Mbah', 'James Michael', 'Sheldon McClellan', 'Metta World']
"""


##### 5. Modify `players_df` with the correct names to re-try a successful merge
# find and map out the correct player mapping;
# this should be done algorithmically, so that in the case there are tons, the maximum amount that can be algorithmically matched / found will be found
player_mapping = {}
mismatched_players = {}

# find and match the perfect subset players into player mapping 
for player in player_misses:
    potential_player_matches = players_df.loc[players_df['name'].str.contains(player), 'name'].values
    if len(potential_player_matches) == 1:
#         print(potential_player_matches[0])
        player_mapping[player] = potential_player_matches[0]
    else:
        mismatched_players[player] = list(potential_player_matches)

# print(player_mapping)
# print(mismatched_players)

# handle the mismatched or unmatched individually;
players_df.loc[players_df['name'].str.contains('Sheldon')]
player_mapping['Sheldon McClellan'] = "Sheldon Mac"
print(player_mapping)

# use the mapping to edit the 'name' columns players_df
for s2017_name, playerdf_name in player_mapping.items():
    players_df.loc[players_df['name'] == playerdf_name, 'name'] = s2017_name

# then merge the tables.
df = s2017_df.merge(players_df, how='left', left_on='Player', right_on='name')
player_misses = list(df.loc[df['name'].isna(), 'Player'])
player_misses # returns []









##### 7. Remove unnecessary columns
df.drop([
    "Year",
    "PER",
    "TS%",
    "3PAr",
    "FTr",
    "USG%",
    "blanl",
    "OWS",
    "DWS",
    "WS",
    "WS/48",
    "blank2",
    "OBPM",
    "DBPM",
    "BPM",
    "VORP",
    "FG%",
    "3P%",
    "eFG%",
    "FT%",
    "name",
], axis=1, inplace=True)



##### 8. Rename teams to their full name
team_mapping = {
    "OKC": "Oklahoma City Thunder",
    "DAL": "Dallas Mavericks",
    "BRK": "Brooklyn Nets",
    "SAC": "Sacramento Kings",
    "NOP": "New Orleans Pelicans",
    "MIN": "Minnesota Timberwolves",
    "SAS": "San Antonio Spurs",
    "IND": "Indiana Pacers",
    "MEM": "Memphis Grizzlies",
    "POR": "Portland Trail Blazers",
    "CLE": "Cleveland Cavaliers",
    "LAC": "Los Angeles Clippers",
    "PHI": "Philadelphia 76ers",
    "HOU": "Houston Rockets",
    "MIL": "Milwaukee Bucks",
    "NYK": "New York Knicks",
    "DEN": "Denver Nuggets",
    "ORL": "Orlando Magic",
    "MIA": "Miami Heat",
    "PHO": "Phoenix Suns",
    "GSW": "Golden State Warriors",
    "CHO": "Charlotte Hornets",
    "DET": "Detroit Pistons",
    "ATL": "Atlanta Hawks",
    "WAS": "Washington Wizards",
    "LAL": "Los Angeles Lakers",
    "UTA": "Utah Jazz",
    "BOS": "Boston Celtics",
    "CHI": "Chicago Bulls",
    "TOR": "Toronto Raptors"
}
df['Team'] = df['Tm'].replace(team_mapping)
df[['Player', 'Tm', 'Team']].head(10)




##### 10. Delete all players from the `TOT` team
# using filtering;
df = df[df['Tm'] != 'TOT']
# alternate method using df.drop condition
df.drop(df.loc[df['Tm'] == 'TOT'].index, inplace=True)


##### 11. What's the team with the most players in the league?
df.groupby('Team')['Team'].value_counts().sort_values(ascending=False)

##### 12. What's the team with the lowest `FG`?
df.groupby('Team')['FG'].sum().sort_values()


##### 13. What's the team with the best `FG%`?
df_fgpct = df[['Player', 'Team', 'FG', 'FGA']].copy()
(df.groupby('Team')['FG'].sum() / df.groupby('Team')['FGA'].sum()).sort_values().tail(5)



##### 14. What's the difference between the best and worst 3P shooters (by position)?
# df.groupby('Pos')
# first we need to get accuracy of 3P
result = (df.groupby('Pos')['3P'].sum()) / (df.groupby('Pos')['3PA'].sum())
result.sort_values(ascending=False)
result.max() - result.min()

# Alternate Answer:
top_3p_by_position = df.groupby('Pos')[['3P', '3PA']].apply(
     lambda rows: rows['3P'].sum() / rows['3PA'].sum()
 ).sort_values(ascending=False)
top_3p_by_position




##### 15. Find the best scorers in each team
# my solution
df[['Player', 'Team', 'Pos', 'PTS']].sort_values(by='PTS', ascending=False)
best_scorer_per_team_list = df.groupby('Team')['PTS'].max()
best_scorers_per_team = pd.merge(df, best_scorer_per_team_list, how='inner', on='PTS')
best_scorers_per_team = best_scorers_per_team[['Player', 'Team', 'Pos', 'PTS']].sort_values(by='PTS', ascending=False)
best_scorers_per_team

# model solution
df["Best Score per Team"] = df.groupby('Team')['PTS'].transform('max')
best_scorers_per_team = df.loc[
    df['PTS'] == df["Best Score per Team"],
    ['Player', 'Team', 'Pos', 'PTS']
].sort_values(by='PTS', ascending=False)
best_scorers_per_team

```



































============================================================================================================
## df.drop
============================================================================================================
The `drop()` method in pandas is used for deleting specified labels from rows or columns of a DataFrame. The method is quite flexible and allows for the dropping of a single label or a list of labels.

### Core Concepts:

- **DataFrame**: A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns) in pandas.
- **Row and Column Labels**: Indices and column names in a DataFrame.
- **In-place Operation**: An operation that modifies the DataFrame directly, without returning a new one.

### Method Signature:

```python
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
```

#### Parameters:

- **labels**: The label(s) to drop.
- **axis**: Axis along which labels will be dropped. `axis=0` (default) for row-wise, `axis=1` for column-wise.
- **index**: Alias for specifying `labels` when dropping rows.
- **columns**: Alias for specifying `labels` when dropping columns.
- **level**: For DataFrames with multi-level index, the level from which to drop.
- **inplace**: If `True`, the DataFrame is modified in place and nothing is returned. Default is `False`.
- **errors**: If 'raise', an error is raised if any of the specified labels are not found in the DataFrame.

### Examples:

#### Dropping a Column:

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print("Original DataFrame:")
print(df)

# Drop column 'A'
df_dropped = df.drop('A', axis=1)
print("DataFrame after dropping column 'A':")
print(df_dropped)
```

#### Dropping a Row:

```python
# Drop row with index label 0
df_dropped = df.drop(0, axis=0)
print("DataFrame after dropping row with index label 0:")
print(df_dropped)
```

#### Dropping Multiple Columns:

```python
# Drop columns 'A' and 'B'
df_dropped = df.drop(['A', 'B'], axis=1)
print("DataFrame after dropping columns 'A' and 'B':")
print(df_dropped)
```

#### Dropping In-Place:

```python
# Drop column 'A' in-place
df.drop('A', axis=1, inplace=True)
print("DataFrame after dropping column 'A' in-place:")
print(df)
```

### Best Practices:

1. **Specify Axis Explicitly**: Always specify the `axis` parameter for clarity, even though it has a default value.
2. **Safety with `inplace`**: Use `inplace=True` with caution, as it will modify the DataFrame in place. Make sure you want to keep the changes.
3. **Handle Errors**: Use the `errors` parameter to specify how to handle errors like non-existent labels.

By understanding how `df.drop()` works, you can efficiently delete rows and columns from a DataFrame according to your data manipulation needs.







============================================================================================================
## df.merge
============================================================================================================
DataFrames in Python's pandas library can be merged using various methods, each serving specific use cases. The primary types of merges include:

1. **Inner Merge**
2. **Left Merge (Left Outer)**
3. **Right Merge (Right Outer)**
4. **Outer Merge (Full Outer)**
5. **Cross Merge**

### Core Concepts:

- **DataFrame**: A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns) in pandas.
  
- **Merge**: Combining DataFrames based on one or more common columns (keys).

#### 1. Inner Merge:

**Use Case**: Combine rows from two DataFrames based on some common column(s) where keys are present in both DataFrames.

**Real-world example**: Suppose you have one DataFrame containing employee IDs and names and another containing employee IDs and salaries. An inner merge would give you a single DataFrame with employee IDs present in both DataFrames along with their names and salaries.

```python
import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [40000, 50000, 60000]})

result = pd.merge(df1, df2, on='ID', how='inner')
# Output: ID      Name  Salary
#         2       Bob  40000
#         3   Charlie  50000
```

#### 2. Left Merge (Left Outer):

**Use Case**: Combine rows from two DataFrames based on a common column(s), including all records from the left DataFrame.

**Real-world example**: Continuing the above example, suppose you want all the employee names and their corresponding salaries if available. Unmatched IDs from the left DataFrame will have `NaN` for the 'Salary' column.

```python
result = pd.merge(df1, df2, on='ID', how='left')
# Output: ID      Name  Salary
#         1     Alice     NaN
#         2       Bob  40000
#         3   Charlie  50000
```

#### 3. Right Merge (Right Outer):

**Use Case**: Similar to the Left Merge but includes all records from the right DataFrame.

**Real-world example**: If you are interested in all employees who have salaries listed, but also want to know if their names are available.

```python
result = pd.merge(df1, df2, on='ID', how='right')
# Output: ID      Name  Salary
#         2       Bob  40000
#         3   Charlie  50000
#         4       NaN  60000
```

#### 4. Outer Merge (Full Outer):

**Use Case**: To get the union of DataFrames, with `NaN` for missing keys on either side.

**Real-world example**: Suppose you want to have a full list of employees, irrespective of whether the salary or name information is available.

```python
result = pd.merge(df1, df2, on='ID', how='outer')
# Output: ID      Name  Salary
#         1     Alice     NaN
#         2       Bob  40000
#         3   Charlie  50000
#         4       NaN  60000
```

#### 5. Cross Merge:

**Use Case**: Creates the Cartesian product of both DataFrames.

**Real-world example**: Imagine you have a DataFrame of Customers and another of Products. You want to know all possible combinations of customers and products, for instance, for a marketing study.

```python
df1 = pd.DataFrame({'Customer': ['A', 'B']})
df2 = pd.DataFrame({'Product': ['P1', 'P2']})
result = pd.merge(df1, df2, how='cross')
# Output:  Customer Product
#         A       P1
#         A       P2
#         B       P1
#         B       P2
```

### Best Practices:

1. **Specify Columns**: Be explicit about the columns on which you're merging, using `left_on` and `right_on` if the column names are different in each DataFrame.

2. **Handle Duplicates**: Before merging, ensure that the key columns don't have duplicates unless it's intentional.

3. **Type Consistency**: Ensure that the columns on which you're merging have the same data type in both DataFrames.

By understanding these different types of merges and when to use them, you can efficiently manipulate your DataFrames to fit various real-world scenarios.

============================================================================================================
## df.groupby('away_team').apply(lambda rows: (rows['result'] == 'A').sum()).sort_values(ascending=False).head()
============================================================================================================
The code performs several operations on a pandas DataFrame (`df`) to find the top away teams based on the number of matches they've won. Let's break it down step by step for a thorough understanding.

### Core Concepts:

1. **DataFrame**: A 2D labeled data structure in pandas.
2. **Grouping**: Segmenting a DataFrame based on a criterion, in this case, `'away_team'`.
3. **Lambda Function**: An anonymous function defined using the `lambda` keyword. Here, it's used to apply a custom operation on each group.
4. **Boolean Masking**: The expression `(rows['result'] == 'A')` produces a boolean Series.
5. **Aggregation**: Using `sum()` to count the number of `True` values, i.e., the number of away wins for each team.

### Steps:

1. **Grouping by 'away_team'**: `df.groupby('away_team')`

    The DataFrame is grouped by the `'away_team'` column. This results in a GroupBy object where each group corresponds to a unique away team.

2. **Applying Lambda Function**: `.apply(lambda rows: (rows['result'] == 'A').sum())`

    For each group (i.e., for each away team), the lambda function is applied. The lambda function does the following:
    - It checks if the `'result'` column is equal to `'A'`, which likely stands for "Away Win". This results in a boolean Series.
    - It then sums this boolean Series, effectively counting the number of `True` values, which represents the number of away wins for the team.

3. **Sorting Values**: `.sort_values(ascending=False)`

    The results are sorted in descending order, so the teams with the most away wins come first.

4. **Top Teams**: `.head()`

    Finally, `head()` is used to get only the top teams (by default, the first 5) based on the number of away wins.

### Example Data:

Let's consider an example DataFrame for context:

```python
import pandas as pd

data = {
    'away_team': ['Team1', 'Team2', 'Team1', 'Team2', 'Team1', 'Team3'],
    'result': ['A', 'H', 'A', 'A', 'H', 'A']
}
df = pd.DataFrame(data)
```

If you run the given code on this DataFrame, you would get:

```
away_team
Team1    2
Team3    1
Team2    1
```

### Best Practices:

1. **Column Selection**: After the `groupby`, be explicit about which columns you need for aggregation. This improves readability and may enhance performance.

2. **Method Chaining**: While method chaining (as done in the code snippet) is convenient, ensure that it doesn't compromise readability.

3. **Commenting**: This is a fairly complex one-liner. In a professional setting, adding a comment that explains what the line does can be very helpful for code maintainability.

Understanding each of these components and best practices provides you with a comprehensive view of what the code is doing and how to use similar constructs effectively.


============================================================================================================
# df.groupby() function
============================================================================================================
The `groupby()` function in the pandas library is a powerful and flexible method used to split the data into groups based on some criteria. Once data is grouped, you can apply various aggregation functions to each group independently. The function is widely used in data analysis and manipulation tasks.

### Core Concepts:

1. **DataFrame**: A 2D labeled data structure in pandas.
2. **Grouping**: Segmenting a DataFrame based on criteria.
3. **Aggregation**: Applying a function to each group of values.

### Syntax:

The basic syntax of `groupby()` is:

```python
DataFrame.groupby(by, axis, level, as_index, sort, group_keys, squeeze, observed)
```

- `by`: Specifies the columns you want to use for grouping.
- `axis`: Specifies the axis along which the function is applied; default is `0` (index).
- `level`: If the axis is a MultiIndex, group by a particular level or levels.
- `as_index`: Whether to return object with group labels as the index; default is `True`.
- `sort`: Sort the groups; default is `True`.
- `group_keys`: When calling `apply`, add group keys to the index to identify pieces; default is `True`.
- `squeeze`: Reduce the dimensionality of the return type if possible, otherwise return a consistent type; default is `False`.
- `observed`: This parameter is useful only when dealing with categorical data. If `True`, only observed categories are returned; default is `False`.

### Basic Usage:

Let's consider a simple DataFrame to illustrate the usage:

```python
import pandas as pd

# Sample DataFrame
data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva'],
        'Salary': [5000, 7000, 5500, 6000, 6500]}

df = pd.DataFrame(data)

# Group by 'Department' and calculate the mean salary for each group
grouped_df = df.groupby('Department')['Salary'].mean()
print(grouped_df)
```

Output:

```
Department
Finance    5500.0
HR         5500.0
IT         6750.0
Name: Salary, dtype: float64
```

### Real-World Example:

Let's assume you have sales data, and you want to find out the total sales for each region for each product:

```python
# Sample DataFrame
data = {'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
        'Product': ['Apple', 'Apple', 'Orange', 'Apple', 'Orange', 'Orange'],
        'Sales': [100, 150, 200, 50, 75, 300]}

df = pd.DataFrame(data)

# Group by 'Region' and 'Product' and sum the 'Sales'
grouped_df = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
print(grouped_df)
```

Output:

```
  Region Product  Sales
0   East   Apple    100
1   East  Orange    275
2   West   Apple    200
3   West  Orange    300
```

### Best Practices:

1. **Column Selection**: After the `groupby` operation, be explicit about which columns you need for aggregation.
  
2. **Reset Index**: After aggregation, it’s usually a good idea to reset the index for the resulting DataFrame using `reset_index()`, unless you have a specific reason to keep the index as-is.

3. **Check Groups**: Before applying an aggregation function, you can check the groups that will be formed by calling the `groups` attribute on the GroupBy object.

By adhering to these practices and understanding the core concepts, you can perform effective data analysis and manipulation using the `groupby()` method in pandas.





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