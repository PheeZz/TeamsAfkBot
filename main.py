'''
pip install pyautogui
pip install numpy
'''
from asyncio.windows_events import NULL
from btnFind import *
from browserPath import *

from random import randint
import numpy as np

import os  # запуск приложений

from pprint import pp, pprint
import yaml

import datetime
import time
import os.path
from multiprocessing import Process
from requests import get

from ui import Ui_Dialog


def getDateTime(date):
    # разбиваем строку date в отдельные значения даты (день\месяц\год\часы\минуты)
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
    startHour = int(time[0]+time[1])
    startMinutes = int(time[3]+time[4])

    startTime = datetime.time(startHour, startMinutes)

    if startTime <= nowToDatetime() <= endTime(time):
        return True
    else:
        return False


def openLessonBrowser(browser, link): webbr.get(browser).open_new_tab(link)


def yandexLesson(link):
    openLessonBrowser('Yandex', link)
    # yandexOpenScript()


def chromeLesson(link):
    openLessonBrowser('Chrome', link)
    scriptBrowser()


    # import app path from txt files
with open('paths/chrome.txt', 'r') as pathFile:
    googlePath = pathFile.read()

with open('paths/yandex.txt', 'r') as pathFile:
    yandexPath = pathFile.read()

with open('paths/msEdge.txt', 'r') as pathFile:
    edgePath = pathFile.read()

with open('paths/teamsApp.txt', 'r') as pathFile:
    teamsAppPath = pathFile.read()


# register browsers names as path

try:
    webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
    webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
    webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))
except Exception as e:
    setBrowserPath()  # function generate browser path if .txt file for Chrome, Yandex, MS Edge, Safari on Windows, MacOS, Linux
finally:
    webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
    webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
    webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))

pastebin = ""
try:
    pathFile = open('paths/pastebin.txt', 'r')
    pastebin = pathFile.read()
except:
    pastebin = 'https://pastebin.com/raw/72t0egj7'
    print("pastebin.txt not found")

# clear current .yml shedule file and parse actual from pastebin
with open('shedule.yml', 'w', encoding='utf-8') as f:
    f.write(get(pastebin).text)
    print('shedule.yml updated successfully')
with open('shedule.yml', 'r', encoding='utf-8') as f:
    shedule = yaml.full_load(f)

today = isoToWeekday(datetime.datetime.today().isoweekday())
print(today)


def sleepUntil(endTime):
    flag = True
    while(flag):
        # защита от дебила, чтобы все одновременно не ливали с пары
        if endTime == nowToDatetime():
            time.sleep(15+randint(0, 20))
            pag.moveTo(500, 500)
            time.sleep(0.5)
            pag.click()
            pag.hotkey('ctrl', 'w')  # close current tab hotkey
            flag = False
            time.sleep(40)
        else:
            time.sleep(30)


while(True):
    if shedule[today]:  # if not empty
        for TimeIters in shedule['Numbering']:
            for subIter in shedule[today]:
                if TimeIters == subIter and isNowBetweenTime(subIter):
                    currentLink = shedule[today][TimeIters]['link']
                    print(currentLink)
                    print('Время окончания текущей пары: ', endTime(TimeIters))
                    chromeLesson(currentLink)
                    # функция, сверяющая время окончания пары с текущим временем
                    sleepUntil(endTime(TimeIters))
                elif TimeIters == subIter and not isNowBetweenTime(subIter):
                    continue
                else:
                    print('Ищу пару на сегодня...')
