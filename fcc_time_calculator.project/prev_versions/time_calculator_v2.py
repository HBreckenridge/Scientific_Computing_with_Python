from datetime import date, timedelta, time, datetime
import time
from time import gmtime, strftime, mktime

def is_am_or_pm(ampm):
    return

def build_time_structure(time):

    inputTimes = [ start, duration ]

    ampm = inputTimes[0].split(" ")[1]

    timeList = [ inputTimes[0].split(" ")[0], inputTimes[1] ]
    totalMins = 0

    aTime = (0000,0,0,5,45,00,6,0,00)
    bTime = (0000,0,0,18,45,00,6,0,00)
    bTimeWDay = (0000,0,0,5,45,00,6,0,00)
    xx = strftime("%I:%M %p %A ", aTime )
    time_A_Format = strftime("%I:%M %p %A", aTime )
    time_B_Format = strftime("%I:%M %p %A", bTime )
    time_B_FormatWithDay = strftime("%I:%M %p %A", bTime )
    print(time_A_Format)
    print(time_B_Format)
    print(time_B_FormatWithDay)
    return


def add_time(start, duration):



    if ampm == str('PM'):
        ampm = 1
    elif ampm == str('AM'):
        ampm = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        
        totalMins += (timeParts[0] * 60 + timeParts[1]) * 60
    totalMins, min = divmod(totalMins, 60)
    hour, min = divmod(totalMins, 60)

    amPMs, hr  = divmod(hour, 12)
    amPMs, currentAMPM = divmod((ampm + amPMs),2)

    ampm = currentAMPM
    days = amPMs / 2
    if ampm == 1:
        ampm = str('PM')
    elif ampm == 0:
        ampm = str('AM')
    if hr == 0:
        hr = 12
    if days <1:
        new_time = ( "%d:%02d %s" % (hr, min, ampm))

        #print (time.strftime("%H:%M",x))
        #print( "%d:%02d %s" % (hr, min, ampm))
    elif days >=1 and days <2:
        daysPast = str("(next day)")
        new_time = ( "%d:%02d %s %s" % (hr, min, ampm, daysPast))
    elif days >=2:
        daysPast = str(days)+str(" days later")    
        new_time = ( "%d:%02d %s %s" % (hr, min, ampm, daysPast))





    return new_time

#print(add_time("2:59 AM", "24:00"))
