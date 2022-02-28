from btnFind import *

import pyscreenshot as ImageGrab
# Used to programmatically control the mouse & keyboard. (эмуляция мыши и клавиатуры)
import pyautogui
import numpy as np
import cv2  # работа с изображениями

import os  # запуск приложений
import webbrowser as webbr

from pprint import pprint

import pickle  # to save\read token file
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

import datetime
import time
import os.path


def getDateTime(date):
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


tmpPath = open('paths/chrome.txt')  # import app path from txt files
googlePath = tmpPath.read()
tmpPath = open('paths/yandex.txt')
yandexPath = tmpPath.read()
tmpPath = open('paths/msEdge.txt')
edgePath = tmpPath.read()
tmpPath = open('paths/teamsApp.txt')
teamsAppPath = tmpPath.read()

# os.startfile(teamsAppPath)
# register browsers names as path
webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))

""" webbr.get('Chrome').open_new_tab('https://vk.com')
webbr.get('Yandex').open_new_tab('https://vk.com')
webbr.get('Edge').open_new_tab('https://vk.com') """

scopes = ['https://www.googleapis.com/auth/calendar.readonly']
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", scopes=scopes)
credentials = pickle.load(open("token.pkl", "rb"))

try:
    service = build("calendar", "v3", credentials=credentials)
except HttpError as error:
    print('An error occurred: %s' % error)

    # засунуть в рефреш на каждую минуту
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
currentCalendar = service.calendarList().list().execute()
calendar_id = currentCalendar['items'][0]['id']
events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                      maxResults=1, singleEvents=True,
                                      orderBy='startTime').execute()

currentClass = events_result['items'][0]['summary']  # геттер "названия" пары
# геттер начала пары
eventStartTime = events_result['items'][0]['start']['dateTime']
link = events_result['items'][0]['location']  # геттер ссылки на пару
arr = np.asarray(getDateTime(eventStartTime)
                 )  # переводим тип turple в массив int'ов с помощью numpy для дальнейшей работы с datetime
eventDateTimeDifference = datetime.datetime(
    arr[0], arr[1], arr[2], arr[3], arr[4])

arr = np.asarray(getDateTime(now))
nowDifference = datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4])
