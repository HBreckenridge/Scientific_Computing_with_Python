from datetime import date, timedelta, time, datetime
import time
from time import gmtime, strftime, mktime

def is_am_or_pm(ampm, hours):
    if ampm == str('PM'):
        hours = hours+12
    elif ampm == str('AM'):
        hours = hours
    return hours

def weekday_int(weekday):
    weekday=weekday.upper()
    if weekday == "MONDAY":
        weekday_int = 0
    elif weekday == "TUESDAY":
        weekday_int = 1
    elif weekday == "WEDNESDAY":
        weekday_int = 2
    elif weekday == "THURSDAY":
        weekday_int = 3
    elif weekday == "FRIDAY":
        weekday_int = 4
    elif weekday == "SATURDAY":
        weekday_int = 5
    elif weekday == "SUNDAY":
        weekday_int = 6
    return weekday_int

def time_div_mod(start, duration):
    timeList = [ start.split(" ")[0], duration ]    
    totalMins = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        
        totalMins += (timeParts[0] * 60 + timeParts[1]) * 60
    totalMins, minutes = divmod(totalMins, 60)
    hours, minutes = divmod(totalMins, 60)
    hours = is_am_or_pm(start.split(" ")[1], hours)
    days, hours = divmod(hours, 24)
    return hours, minutes, days

def build_time_structure(hours, minutes, days, day_int, display_weekday=False):
    day = days+day_int
    total_time = (0000,0,0,hours,minutes,00,day,0,00)
    if display_weekday == False:
        time_formatted = strftime("%I:%M %p", total_time )
    elif display_weekday == True:
        time_formatted = strftime("%I:%M %p %A", total_time )
    return day, time_formatted




def add_time(start, duration, weekday=None):
    if weekday != None:
        day_int = weekday_int(weekday)
        display_weekday = True
    elif weekday == None:
        day_int = 0
        display_weekday = False
    hours, minutes, days = time_div_mod(start, duration)
    days, time_formatted = build_time_structure(hours, minutes, days, day_int, display_weekday)


    #if hr == 0:
    #    hr = 12
    if days <1:
        add_time_result = time_formatted
    if days >=1 and days <2:
        daysPast = str("(next day)")
        add_time_result = time_formatted+" "+daysPast
    elif days >=2:
        daysPast = "("+str(days)+str(" days later)")    
        #new_time = ( "%d:%02d %s %s" % (hr, min, ampm, daysPast))
        add_time_result = time_formatted+" "+daysPast





    return add_time_result
#build_time_structure("11:30 AM", "2:32", "Monday")
#print(add_time("11:30 AM", "300:02", "Monday"))
print(add_time("8:16 PM", "466:02"))
#expected = "6:18 AM (20 days later)"
