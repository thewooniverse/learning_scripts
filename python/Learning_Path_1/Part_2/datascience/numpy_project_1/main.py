import numpy as np
import datetime, calendar
import pandas as pd
import matplotlib.pyplot as plt

# create / import the dataset
year = 2021
temperatures = np.random.randint(-5,37, size=365)


# 2. **Calculate Basic Statistics:**
#    - Find the mean, median, and standard deviation of the temperatures.
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
std_temp = np.std(temperatures)

print(f"Mean Temp: {mean_temp}\nMedian Temp: {median_temp} \nStandard Deviation: {std_temp}")

#    - Identify the hottest and coldest days.
hottest_day = np.max(temperatures)
coldest_day = np.min(temperatures)
print(f"The hottest day of the year was: {np.argmax(temperatures)}th day with {hottest_day} celsius!\n The coldest day of the year was:{np.argmin(temperatures)}th day of the year measuring {coldest_day}celsius")


# 3. **Monthly Analysis:**
#    - Divide the data into 12 months, assuming 30 days for simplicity.
#    - Calculate the average temperature for each month.
## dividing the month using slicing and datetime module to calculate for the year.

month_days = {}
total_days = 0

for month in range(1, 13):  # Iterate through all months (1 to 12)
    _, num_days = calendar.monthrange(year, month)  # Returns the number of days in the month
    # print(f"Month {month}: {num_days} days")
    total_days += num_days
    month_days[f'{month}'] = (num_days, total_days)

print(month_days)

# now that we have the dates... we can loop through each of them;
monthly_mean = {}
monthly_median = {}
monthly_std = {}
monthly_min = {}
monthly_max = {}

for month, (num_days, total_days) in month_days.items():
    # slice the dataset
    month_subset = temperatures[(total_days-num_days):(total_days)]
    monthly_mean[month] = np.mean(month_subset)
    monthly_median[month] = np.median(month_subset)
    monthly_std[month] = np.std(month_subset)
    monthly_max[month] = np.max(month_subset)
    monthly_min[month] = np.min(month_subset)

    print(f"""\n\n---
    Month {month} temperature stats:
    mean: {np.mean(month_subset)}
    median: {np.median(month_subset)}
    standard dev: {np.std(month_subset)}
    max temp: {np.max(month_subset)}
    min temp: {np.min(month_subset)}

    dataset: {month_subset}
---""")

####
monthly_temps = []
for month, mean_temp in monthly_mean.items():
    monthly_temps.append(mean_temp)
monthly_temps = np.array(monthly_temps)


plt.figure(figsize=(10,6))
# plt.plot(temperatures, marker='o', linestyle='-', color='b')  # Plotting the sales data
plt.plot(monthly_temps, marker='o', linestyle='-', color='r')
plt.title("Temperatures over 2021")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()






## dividing the month using pandas dataframe
# date_range = pd.date_range(start="1/1/2021", end='12/31/2021', freq='D')
# df = pd.DataFrame(date_range, columns=['date'])
# df['temperature'] = temperatures
# df.set_index('date', inplace=True)
# print(df)

# monthly_temperatures = df.resample('M').mean()
# print(monthly_temperatures)