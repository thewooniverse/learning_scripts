import numpy as np
import pandas as pd
import os





# 0. Load from the London weather series and play around with the indexes
weather_df = pd.read_csv(f'{os.getcwd()}{os.path.sep}london_weather.csv')
# print(weather_df)


# 1. Create a new series with random numbers
random_series = pd.Series(np.random.randn(10))
print(random_series)

random_series = pd.Series(np.random.randn(10), index=['a','b','c','d','e','f','g','h','i','j'])
print(random_series)



# 2. Create a new dataframe with random numbers



