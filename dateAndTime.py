import datetime


def getDateTime(date):
    '''разбиваем строку date в отдельные значения даты (день\месяц\год\часы\минуты)'''
    iterator = 0
    str_year, str_month, str_day, str_hours, str_minutes = "", "", "", "", ""
    while iterator < 4:
        str_year += date[iterator]
        iterator += 1
    iterator = 0
    while iterator < 2:
        str_month += date[5+iterator]
        str_day += date[8+iterator]
        str_hours += date[11+iterator]
        str_minutes += date[14+iterator]
        iterator += 1
    year, month, day, hours, minutes = int(str_year), int(
        str_month), int(str_day), int(str_hours), int(str_minutes)
    return year, month, day, hours, minutes


def timeNow(): return datetime.datetime.utcnow().isoformat()


def isoToWeekday(digit):
    # перевод "цифрового" представления о текущем дне недели в текстовый
    # для сравения с инфой в shedule.yml
    if digit == 1:
        return 'Monday'
    elif digit == 2:
        return 'Tuesday'
    elif digit == 3:
        return 'Wednesday'
    elif digit == 4:
        return 'Thursday'
    elif digit == 5:
        return 'Friday'
    elif digit == 6:
        return 'Saturday'
    elif digit == 7:
        return 'Sunday'


def getTimeNow():
    now = str(datetime.datetime.now().time())
    nowHour = int(now[0]+now[1])
    nowMinutes = int(now[3]+now[4])
    nowTime = datetime.time(nowHour, nowMinutes)
    return nowTime


def nowToDatetime():
    now = str(datetime.datetime.now().time())
    nowHour = int(now[0]+now[1])
    nowMinutes = int(now[3]+now[4])
    nowTime = datetime.time(nowHour, nowMinutes)
    return nowTime


def endTime(time):
    endHour = int(time[6]+time[7])
    endMinutes = int(time[9]+time[10])
    endTime = datetime.time(endHour, endMinutes)
    return endTime


def isNowBetweenTime(time):
    '''return True or False if NOW is between time argument'''
    startHour = int(time[0]+time[1])
    startMinutes = int(time[3]+time[4])

    startTime = datetime.time(startHour, startMinutes)

    if startTime <= nowToDatetime() <= endTime(time):
        return True
    else:
        return False


def updateToday():
    '''return today's weekday'''
    return isoToWeekday(datetime.datetime.today().isoweekday())
