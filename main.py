'''
pip install pyautogui
pip install requests
pip install opencv-python
pip install pyYAML
pip install pygetwindow
'''
from time import sleep
from browserPath import *
from dateAndTime import isNowBetweenTime
from lessonClass import *
from windowsCalculator import *
from btnFind import waitGetAllConnectButtons

import yaml
import os.path
from requests import get
from multiprocessing import Process
from threading import Thread


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


# import app path from txt files
try:
    with open('userData/paths.yaml', 'r') as file:
        paths = yaml.full_load(file)
except Exception as e:
    with open('userData/paths.yaml', 'w') as file:  # recreate file
        pass
        setBrowserPath()
    with open('userData/paths.yaml', 'r') as file:
        paths = yaml.full_load(file)

googlePath = paths['Google']
yandexPath = paths['Yandex']
edgePath = paths['Edge']
teamsAppPath = paths['Teams']

# register browsers names as path
webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))

pastebin = ""
try:
    pathFile = open('userData/pastebin.txt', 'r')
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


def createTasksList(shedule, lessonStartTime):
    processes = list()

    for index in range(len(whichAppsLaunch())):
        proc = Lesson(browser=whichAppsLaunch()[index], box=getBoxes()[index])
        proc.getLessonInfoFromShedule(shedule, lessonStartTime)
        processes.append(proc)
    return processes


def waitAnimate(index):
    if index == 0:
        print('Ищу следущую пару.')
        index += 1
        time.sleep(0.5)
    elif index == 1:
        print('Ищу следущую пару..')
        index += 1
        time.sleep(0.5)
    elif index == 2:
        print('Ищу следущую пару...')
        time.sleep(0.5)
        clearConsole()
        index = 0
    return index


def launchAppsFromList(listOfLaunch, processes):
    for app in listOfLaunch:
        proc = Thread(target=app.launch())
        processes.append(proc)
        proc.start()


def connectAppsFromList(listOfLaunch, processes):
    for app in listOfLaunch:
        proc = Thread(target=app.connect())
        processes.append(proc)
        proc.start()


def sleepAppsFromList(listOfLaunch, processes):
    for app in listOfLaunch:
        proc = Thread(target=app.sleep())
        processes.append(proc)
        proc.start()


def sleepMainProcessUntilEndtime(lessonStartTime):
    flag = True
    while(flag):
        if not isNowBetweenTime(lessonStartTime):
            flag = False
        else:
            time.sleep(60)


def __main__(currentLesson=Lesson(), shedule=shedule):
    while(True):
        today = dt.updateToday()
        if shedule[today]:  # if not empty
            index = 0
            for numbers in shedule['Numbering']:
                for lessonStartTime in shedule[today]:
                    if numbers == lessonStartTime and dt.isNowBetweenTime(lessonStartTime):
                        clearConsole()
                        currentLesson.getLessonInfoFromShedule(
                            shedule, lessonStartTime)
                        print(currentLesson)

                        for browser in whichAppsLaunch():
                            openLessonBrowser(browser, 'google.com')
                        time.sleep(1)
                        runningApps = whichAppsLaunch()
                        listOfLaunch = list()
                        index = 0
                        for currentApp in runningApps:
                            runIt = Lesson()
                            runIt.getLessonInfoFromShedule(
                                shedule, lessonStartTime)
                            runIt.browser = currentApp
                            if len(runningApps) > 1:
                                runIt.setBox(getBoxes()[index])
                            else:
                                runIt.setBox(fullscreen)
                            listOfLaunch.append(runIt)
                            index += 1
                        processes = list()
                        time.sleep(1)
                        for apps in listOfLaunch:
                            apps.launch()

                        waitGetAllConnectButtons(currentLesson.link)

                        for apps in listOfLaunch:
                            apps.connect()

                        for apps in listOfLaunch:
                            apps.sleep()

                    else:
                        index = waitAnimate(index)

        else:
            print('Нет онлайн пар на сегодня.')
            time.sleep(3600)


__main__()
