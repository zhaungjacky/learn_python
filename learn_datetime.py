import datetime
import pytz



# dt= datetime.datetime(2024,6,11,5,44,58,tzinfo=pytz.UTC)

dt_utc_now= datetime.datetime.now(tz=pytz.UTC) # cool one

dt_mtn = dt_utc_now.astimezone(pytz.timezone('US/Pacific'))
# for tz in pytz.all_timezones:
#     print(tz)
# dt_utc= datetime.datetime.now(datetime.UTC).replace(tzinfo=pytz.UTC)


# print(dt)
print(dt_utc_now)
# dt= datetime.datetime(2024,6,11,5,44,58,100)


# print(dt.time())
# d = datetime.datetime.now()
# tday = datetime.date.today()
# # print(d)
# # print(tday)

# tdelta = datetime.timedelta(7)

# bday = datetime.date(2025,3,4)

# t_bday = bday - tday

# print(t_bday.days)
# print(t_bday.total_seconds())

# print(tday - tdelta)