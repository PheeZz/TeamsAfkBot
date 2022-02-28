import pyscreenshot as ps
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
import os.path


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'CALENDAR'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

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
events = events_result.get('items', [])

currentClass = events_result['items'][0]['summary']
eventStartTime = events_result['items'][0]['start']['dateTime']
