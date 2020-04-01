import datetime
import pytz

#Describing the date,weekday and isoweekday for monday
d=datetime.date(2019,5,13)
print(d)

#Monday starts for count as 0 and sunday as 6
print(d.weekday())

#Monday as 1 and sunday as 7
print(d.isoweekday())

#Shows today date and time
d=datetime.datetime.today()
print(d)

#Shows today date,day,month and year
d=datetime.date.today()
print(d)
print(d.day)
print(d.month)
print(d.year)

tdel=datetime.timedelta(days=7)
print("today:",d,". After 7days: ",d+tdel)

#date=date+timedelta
#timedelta=datea+dateb
bday=datetime.date(1998,9,14)
till_date=d-bday
print(till_date)
print(till_date.days)
print(till_date.total_seconds())

#Time formatting
t=datetime.time(9,50,59,1000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

#Datetime formatting
dt=datetime.datetime(2019,5,1,20,31,20,10000)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt)

delt=datetime.timedelta(days=7,hours=12)
adddt=dt+delt
print(adddt)
print()

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

#This shows at microseconds like 20+00:00 which is utc offset
dt=datetime.datetime(2019,5,1,20,31,20, tzinfo=pytz.UTC)
print(dt)

#Shows the current utc time where milisecond added like 42.484065+00:00 
#and timezone aware
dt_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

#Almost the same as before but better to prefer above ones
dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

#To set timezone into our location zone like 2019-05-13 11:31:22.968456-04:00
#minus sign show the difference between mine and us/eastern
dt_mtn=dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)

#Shows all the timezones location as above like 'US/Eastern'
for timezones in pytz.all_timezones:
	print(timezones)

#Timezone aware
dt_nowtz=datetime.datetime.now(tz=pytz.UTC)
print(dt_nowtz)

#Timezone unaware
dt_now=datetime.datetime.now()
print(dt_now)

#Naive datetime whice is unavaired of utc
dt_now=datetime.datetime.now()
print(dt_now)
mnt=pytz.timezone('US/Eastern')

#Making the unavariable naive into local pytz timezone
dt_nowtz=mnt.localize(dt_now)
print(dt_nowtz)

#strftime converts datetime into string
dt=datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
print(dt.strftime('%B %d,%Y'))

#strptime converts string to datetime
str_dt='May 13,2019'
dt=datetime.datetime.strptime(str_dt,'%B %d,%Y')
print(dt)