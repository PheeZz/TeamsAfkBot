from btnFind import *

import pyscreenshot as ImageGrab
# Used to programmatically control the mouse & keyboard. (эмуляция мыши и клавиатуры)
import pyautogui
import numpy as np
import cv2  # работа с изображениями

import os  # запуск приложений
import webbrowser as webbr

from pprint import pp, pprint
import yaml

import datetime
import time
import os.path
from multiprocessing import Process
from requests import get


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


def isNowBetweenTime(time):
    startHour = int(time[0]+time[1])
    startMinutes = int(time[3]+time[4])
    endHour = int(time[6]+time[7])
    endMinutes = int(time[9]+time[10])

    now = str(datetime.datetime.now().time())
    nowHour = int(now[0]+now[1])
    nowMinutes = int(now[3]+now[4])

    startTime = datetime.time(startHour, startMinutes)
    endTime = datetime.time(endHour, endMinutes)
    nowTime = datetime.time(nowHour, nowMinutes)

    if startTime <= nowTime <= endTime:
        return True
    else:
        return False


def openLessonBrowser(browser, link): webbr.get(browser).open_new_tab(link)

""" webbr.get('Chrome').open_new_tab('https://vk.com')
webbr.get('Yandex').open_new_tab('https://vk.com')
webbr.get('Edge').open_new_tab('https://vk.com') """

# import app path from txt files
with open('paths/chrome.txt', 'r') as pathFile:
    googlePath = pathFile.read()

with open('paths/yandex.txt', 'r') as pathFile:
    yandexPath = pathFile.read()

with open('paths/msEdge.txt', 'r') as pathFile:
    edgePath = pathFile.read()

with open('paths/teamsApp.txt', 'r') as pathFile:
    teamsAppPath = pathFile.read()

# os.startfile(teamsAppPath)
# register browsers names as path
webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))

today = isoToWeekday(datetime.datetime.today().isoweekday())
# засунуть в рефреш на каждую минуту
now = datetime.datetime.utcnow().isoformat()
arr = np.asarray(getDateTime(now))
# переводим тип turple в массив int'ов с помощью numpy для дальнейшей работы с datetime
nowDifference = datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4])
print(nowDifference)

# очистка файла с расписанием и парсинг актуального с pastebin
with open('shedule.yml', 'w', encoding='utf-8') as f:
    f.write(get('https://pastebin.com/raw/72t0egj7').text)
with open('shedule.yml', 'r', encoding='utf-8') as f:
    shedule = yaml.full_load(f)

for Iter in shedule['Numbering']:
    for subIter in shedule[today]:
        if Iter == subIter and isNowBetweenTime(subIter):
            print("True")
        else:
            print("False")
