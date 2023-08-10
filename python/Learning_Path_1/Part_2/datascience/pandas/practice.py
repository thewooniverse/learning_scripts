import pandas as pd
import os


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
# print(df)
# print(df['name']) # prints the name column, Name: name, dtype: object
# df.to_excel(f'{os.getcwd()}{os.path.sep}df.xlsx')

name_column = df['name']
subset = df[['name', 'location']]
# print(subset)

jack = df.iloc[0:1] # selects the row
# print(jack) 




# get the group of people older than 21
legal_drinkers = df[df['age']>21]
# print(legal_drinkers['name'])
mean_age = df['age'].mean()
print(mean_age)
median_age = df['age'].median()
print(median_age)


data1 = {
    'name': ['susan', 'karen', 'johnson'],
    'age': [69, 42, None],
    'location': ['Mohson Kahni', 'Johnsonville', 'Toronto']
}
df1 = pd.DataFrame(data1)

combined = pd.concat([df, df1])
# print(combined)

dropped_df = combined.dropna()
# print(dropped_df) # removes johnson that does not have a age.

filled_df = combined.fillna(value=21)
# print(filled_df) # replaces NaN value with 21 for johnson





