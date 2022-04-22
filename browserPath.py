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
        addThis = f'Google: {googlePath}\n'
        f = open('userData/paths.yaml', 'a')
        f.write(addThis)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден chrome, вы можете попробовать задать путь вручную в файле userData/paths.yaml')


def setYandexPath():
    try:
        yandexPath = findPath('browser.exe', '\\')
        addThis = f'Yandex: {yandexPath}\n'
        f = open('userData/paths.yaml', 'a')
        f.write(addThis)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден browser.exe в папке, вы можете попробовать задать путь вручную в файле userData/paths.yaml')


def setEdgePath():
    try:
        edgePath = findPath('msedge.exe', '\\')
        addThis = f'Edge: {edgePath}\n'
        f = open('userData/paths.yaml', 'a')
        f.write(addThis)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден msedge.exe в папке, вы можете попробовать задать путь вручную в файле userData/paths.yaml')


def setSafariPath():
    try:
        safariPath = findPath('safari.exe', '\\')
        addThis = f'safariPath: {safariPath}\n'
        f = open('userData/paths.yaml', 'a')
        f.write(addThis)
        f.close()
    except Exception as e:
        print(e)
        print('Не найден safari, вы можете попробовать задать путь вручную в файле userData/paths.yaml')


def setTeamsPath():
    try:
        teamsFile = "\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
        addThis = f'Teams: \\Users\\{os.getlogin()}{teamsFile}\n'
        f = open('userData/paths.yaml', 'a')
        f.write(addThis)
        f.close()
    except Exception as e:
        print(e)
        print("Не найден Teams/Update.exe, вы можете попробовать задать путь вручную в файле userData/paths.yaml")


def setBrowserPath():
    if getSystem() == 'Windows':
        startTime = datetime.now()
        setChromePath()
        setYandexPath()
        setEdgePath()
        setTeamsPath()
        print(datetime.now() - startTime)

    elif getSystem() == 'Darwin':
        setSafariPath()
        setChromePath()

    elif getSystem() == 'Linux':
        setChromePath()

    elif getSystem() == 'Unknown':
        print('Uncnown system')
