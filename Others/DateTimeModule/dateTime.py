# date time module

# import datetime

# d = datetime.date(2018,3,19)
# print(d)

# tday = datetime.date.today()
# print(tday.day)   
# for months tday.year for day tday.date 

# weekday -> monday is 0  sunday is 6  (tday.weekday())
# isoweekday -> modnay is 1 sunday is 7 (tday.isoweekday())


# timedelte is different between two dates

# tdelta =  datetime.timedelta(days = 7)
# get the current data + 7 days 
# print(tday + tdelta)
# print(tday - tdelta)



# date2 = data1 + timedelta
# timedelta = data1 + date2

# bday = datetime.date(2019,9,16)

# till_bday = bday - tday
# print(till_bday)




# <!--------------time module------------------!>

import datetime
import pytz 
# dt = datetime.datetime(2019,3,19,9,30,45,1000)
# tdelta = datetime.timedelta(hours = 12)
# tdelta = datetime.timedelta(days = 7)

# print(dt + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# <!----------------using Pytz--------------------------!>

# dt = datetime.datetime(2019,3,19,9,35,45, tzinfo = pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)


# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
# print(dt_utcnow)

#  