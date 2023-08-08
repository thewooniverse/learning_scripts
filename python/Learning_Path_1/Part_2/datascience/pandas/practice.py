import pandas as pd


s1 = pd.Series([3, 5, 6, 9], index=['a', 'b', 'c', 'd'])
s2 = pd.Series(["nyc", "Jackson", 32, 5912], index=['location', 'name', 'age', 'dev_score'])
# print(s2) # prints the whole table
# print(s2['location']) # prints nyc


data = {
    'name': ['jack', 'daniel', 'becky'],
    'age': [50, 30, 19],
    'location': ['New York City', 'Jacksonville', 'Maryland']
}
df = pd.DataFrame(data)
print(df)
print(df['name']) # prints the name column, Name: name, dtype: object


