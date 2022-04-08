import platform
import os
from datetime import datetime


def getSystem():
    if platform.system() == "Windows":
        return 'Windows'
    elif platform.system() == "Darwin":
        return 'Mac'
    elif platform.system() == "Linux":
        return 'Linux'
    else:
        return 'Unknown'


def findPath(name, path):
    for dirpath, dirname, filenames in os.walk(path):
        if name in filenames:
            return os.path.join(dirpath, name)


def setChromePath():
    try:
        googlePath = findPath('chrome.exe', '\\')
        f = open('paths/chrome.txt', 'w')
        f.write(googlePath)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден chrome, вы можете попробовать задать путь вручную в файле paths/chrome.txt')


def setYandexPath():
    try:
        yandexPath = findPath('browser.exe', '\\')
        f = open('paths/yandex.txt', 'w')
        f.write(yandexPath)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден browser.exe в папке, вы можете попробовать задать путь вручную в файле paths/yandex.txt')


def setMsEdgePath():
    try:
        edgePath = findPath('msedge.exe', '\\')
        f = open('paths/msEdge.txt', 'w')
        f.write(edgePath)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден msedge.exe в папке, вы можете попробовать задать путь вручную в файле paths/msEdge.txt')


def setSafariPath():
    try:
        safariPath = findPath('safari', '\\')
        f = open('paths/safari.txt', 'w')
        f.write(safariPath)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден safari, вы можете попробовать задать путь вручную в файле paths/safari.txt')


def setBrowserPath():
    if getSystem() == 'Windows':
        startTime = datetime.now()
        setChromePath()
        setYandexPath()
        setMsEdgePath()
        print(datetime.now() - startTime)

    elif getSystem() == 'Darwin':
        setSafariPath()
        setChromePath()

    elif getSystem() == 'Linux':
        setChromePath()

    elif getSystem() == 'Unknown':
        print('Uncnown system')


setBrowserPath()
