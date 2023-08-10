import pandas as pd

# 1. **Load the Data:** Read the data into a NumPy array. 
# You may need to preprocess it to remove missing values or to convert certain columns to the correct data type.

df = pd.read_csv('london_weather.csv')
print(df)

# 2. **Basic Statistics:** Calculate basic statistics for each weather attribute (mean, median, standard deviation, etc.).
# This will give you an overall idea of the weather patterns in the location.

# statistics over whole period

# statistics over subset of time period (2019-2020)
daily_mean_temp_mean = df['mean_temp'].mean()
daily_mean_temp_std = df['mean_temp'].std()
daily_mean_temp_median = df['mean_temp'].median()

# print(daily_mean_temp_mean, daily_mean_temp_std, daily_mean_temp_median)

daily_sunshine_mean = df['sunshine'].mean()
daily_sunshine_std = df['sunshine'].std()
daily_sunshine_median = df['sunshine'].median()

# print(daily_sunshine_mean, daily_sunshine_std, daily_sunshine_median)




# 3. **Temperature Analysis:** Analyze temperature variations throughout the year. 
# You can calculate monthly averages, identify the hottest and coldest days, and look for any unusual spikes or drops.

# change the dataframe date column into a date format
# Convert the 'date' column to a datetime type
df['date'] = pd.to_datetime(df['date'])

# Set the 'date' column as the index
df.set_index('date', inplace=True)
print(df)
monthly_data = df.resample('M')