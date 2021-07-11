import datetime


tday = datetime.date.today()
print(tday.year)                # 2018
print(tday.month)               # 11
print(tday.day)                 # 26

print(tday.weekday())           # 0
print(tday.isoweekday())         # 1
# weekday MONDAY :0, SUNDAY :6
# iso weekday MONDAY:1 SUNDAY:0

# # # ############
#  tdelta
#################
tdelta = datetime.timedelta(days=7)
print(tday +tdelta)                 # 2018-12-03
print(tday - tdelta)                #  2018-11-19
bday = datetime.date(2018,8,25)
till_day = bday-tday
print(till_day)                     # -93 days, 0:00:00
print(till_day.total_seconds())     # -8035200.0

###############3
# time
################

t = datetime.time(9, 30, 45, 100000)  #  hh,mm,ss,micro ss
print(t)                  #  09:30:45.100000
print(t.hour)               # 9
print(t.minute)             # 30
print(dir(t))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fold', 'hour', 'isoformat', 'max', 'microsecond', 'min', 'minute', 'replace', 'resolution', 'second', 'strftime', 'tzinfo', 'tzname', 'utcoffset']
print(t.min)                # 00:00:00
print(t.minute)             # 30

############
#  DATE TIME
######################333

dt= datetime.datetime(2018,7,28,12,30,45,10000)
print(dt)           # 2018-0-28 12:30:45.010000



t= datetime.datetime(2018,11,28,12,30,45,10000)
print(t)            # 2018-11-28 12:30:45.010000
print(t.date())     # 2018-11-28
print(t.time())     # 12:30:45.010000
print(t.year)       # 2018
print(t.month)      # 11
print(t.day)        # 28


tdelta = datetime.timedelta(days=7)
print(t +tdelta)        # 2018-12-05 12:30:45.010000
tdelta = datetime.timedelta(hours=12)
print(t +tdelta)        # 2018-11-28 19:30:45.010000



##########################3333
##
#################################

dt_today = datetime.datetime.today()        # current local time NO-TIMEZOME
dt_now = datetime.datetime.now()            # give TIMEZONE : default: NONE
dt_utcnow = datetime.datetime.utcnow()      # UTC info: NONE

print("Today:\t", dt_today)             # 2018-11-26 21:20:31.829934
print("now:\t",  dt_now)                # 2018-11-26 21:20:49.192463
print("utcnow:\t",dt_utcnow)            # 2018-11-26 15:51:51.149416


##

# https://docs.python.org/3/library/datetime.html
# dateulti.tz   libray IANA timezone database
# pytz          library IANA timezone database



# pip install pytz

# In pytz : always recommend to use UTC
import pytz
print ('Timezone')
#


#

dt_dtz = datetime.datetime.now(tz=pytz.UTC)
print ("time zone defalut :\t", dt_dtz)
dt_UsMountain_tz = dt_dtz.astimezone(pytz.timezone('Asia/Kolkata')) # US/Mountain
print("time zone US/Moun : \t", dt_UsMountain_tz)                                 # 2018-11-26 13:36:10.214904-07:00



# given naive datetime to timezone

dt_naive = datetime.datetime.now()
# print(dt_naive)                                         # 2018-11-27 02:10:09:10.0000
UsMountain_tz = pytz.timezone('US/Mountain') 
# print(UsMountain_tz)                                    # US/Mountain
dt_UsMountain_tz = UsMountain_tz.localize(dt_naive)
print("time zone US/Moun : \t",dt_UsMountain_tz)                                # 2018-11-27 02:10:19.941388-07:00

## Display, pass : ISO Formate()

print(dt_UsMountain_tz.isoformat())

# time fomate to sting
print(dt_UsMountain_tz.strftime('%B %d, %Y'))

# string Predict+3.
# time strptime

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)