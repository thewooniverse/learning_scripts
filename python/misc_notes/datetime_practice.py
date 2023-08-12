import datetime

today = datetime.date.today()
now = datetime.datetime.now()

d = datetime.date(2023, 5, 6)
t = datetime.time(14, 32, 50, 30)
dt = datetime.datetime(2033, 3, 4, 5, 55, 2)


delta = datetime.timedelta(days=5, minutes=35, hours=8)
future_date = now + delta
past_date = today - delta
print(future_date, today, past_date)

formatted = now.strftime('%Y-%m-%d')
formatted_2 = future_date.strftime('%d-%m-%Y %H:%M:%S')
print(formatted)
print(formatted_2)



# create a logger class to test out the functionality of the banking app logging
# tbqh, I don't think I even need to test it
# when at the creation event of the account, it will do xyz, and the same with the cosntruction of the customer object
# just need to get a refersher on timedelta object.




