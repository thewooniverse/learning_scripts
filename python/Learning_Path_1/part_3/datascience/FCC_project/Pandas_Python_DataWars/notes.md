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




