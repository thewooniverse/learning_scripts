import pandas as pd
import os








# loading a dataframe from a dictionary

data = {
    'name' : ['johnson', 'becky', 'karen'],
    'age': [32, 55, 69],
    'city': ['almaty', 'johannesburg', 'cape town']
}

df = pd.DataFrame(data)
print(df)


# loading a dataframe from a list of lists and assigning a column to each;
# data = [
#     ['johnson', 'becky', 'karen'],
#     [32, 55, 69],
# ['almaty', 'johannesburg', 'cape town']] this is an incorrect way of handling this, the correct way for data to be would be

data = [
    ['john', 32, 'almaty'],
    ['becky', 55, 'johannesburg'],
    ['karen', 69, 'cape town'],
    ['bossa', 10, 'cape town']
] # loading it from a list of lists they need to be in the rows format;



df = pd.DataFrame(data, columns=['name', 'age', 'city'])
print(df)

# print(df[['name','city']])
# print(df.loc[0][0]) #johnson
# print(df.iloc[1][0]) #32

# print(f"AGE IS {df[['age']].loc[0]}")


df['job'] = ['Engineer', 'Janitor', 'Assistant Regional Manager', 'current child']
df['SAT_score'] = [1500, 100, 300, None]
# print(df)

# df.drop('job', axis=1, inplace=True)
# print(df) # drops the whole column
# df.drop(0, inplace=True)
# print(df) # drops the whole name row

older_than_50 = df[df['age'] > 50]
print(older_than_50) # returns the two rows, becky, kraen that are older than
print(older_than_50[['name']]) # returns a column with just names becky, karen

sorted_by_age = df.sort_values(by='age')
print(sorted_by_age)

print(df.describe())

group_by_city = df.groupby('city').size()
print(group_by_city)
# print(df)
df.fillna(0, inplace=True)
print(df) # switches the SAT_score=NaN for bossa to 0




loaded_df = pd.read_csv(f'{os.getcwd()}{os.path.sep}london_weather.csv')
print(loaded_df.describe())









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
# print(mean_age)
median_age = df['age'].median()
# print(median_age)


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





