import datetime
import pytz

today = datetime.date.today()
now = datetime.datetime.now()

d = datetime.date(2023, 5, 6)
t = datetime.time(14, 32, 50, 30)
dt = datetime.datetime(2033, 3, 4, 5, 55, 2)


delta = datetime.timedelta(days=5, minutes=35, hours=8)
future_date = now + delta
past_date = today - delta
# print(future_date, today, past_date)

formatted = now.strftime('%Y-%m-%d')
formatted_2 = future_date.strftime('%d-%m-%Y %H:%M:%S')
# print(formatted)
# print(formatted_2)


year = today.year
month = today.month
day = today.day
hour = now.hour

new_dt = dt.replace(year=2049)
print(dt)
print(new_dt)

diff = new_dt - dt
in_minutes = diff.total_seconds() / 60
print(f"in hours is {diff.total_seconds()}, in minutes its {in_minutes}, in hours is {in_minutes/60}, in days its {(in_minutes/60)/24}")


weekday_num = today.weekday()
print(weekday_num)

iso_format = today.isoformat()
print(iso_format)





tz = pytz.timezone('US/Eastern')
eastern_time = tz.localize(datetime.datetime.now())
print(datetime.datetime.now())
print(eastern_time)

utc_time = eastern_time.astimezone(pytz.utc)
# print(utc_time)



# create a logger class to test out the functionality of the banking app logging
# tbqh, I don't think I even need to test it
# when at the creation event of the account, it will do xyz, and the same with the cosntruction of the customer object
# just need to get a refersher on timedelta object.




