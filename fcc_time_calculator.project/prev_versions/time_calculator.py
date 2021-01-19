from datetime import date, timedelta, time
import time

def add_time(start, duration):


    inputTimes = [ start, duration ]

    ampm = inputTimes[0].split(" ")[1]

    timeList = [ inputTimes[0].split(" ")[0], inputTimes[1] ]
    totalMins = 0

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

print(add_time("2:59 AM", "24:00"))
