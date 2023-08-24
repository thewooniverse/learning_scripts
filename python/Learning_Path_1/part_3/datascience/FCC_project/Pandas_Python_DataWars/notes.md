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



