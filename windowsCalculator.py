from btnFind import *
from lessonClass import *
import yaml

kWidth = int(pag.size()[0]/1920)  # опитимизация под разные разрешения
kHeight = int(pag.size()[1]/1080)


def optimizeBox(box):
    box[0] *= kWidth
    box[1] *= kHeight
    box[2] *= kWidth
    box[3] *= kHeight
    return box


upperBox = optimizeBox([0, 0, 1920, 360])
lowerBox = optimizeBox([0, 600, 1920, 380])
midBox = optimizeBox([0, 350, 1920, 350])
logoBox = optimizeBox([0, 0, 250, 150])
leftUpBox = optimizeBox([0, 0, 960, 540])
leftDownBox = optimizeBox([0, 540, 960, 540])
rightUpBox = optimizeBox([960, 0, 960, 540])
rightDownBox = optimizeBox([960, 540, 960, 540])
fullscreen = optimizeBox([0, 0, 1920, 1080])
splitscreenLeft = optimizeBox([0, 0, 960, 1080])
splitscreenRight = optimizeBox([960, 0, 960, 1080])


def getAnswerBool(answer):
    '''get answer from user'''
    if answer == '' or answer == 'y' or answer == 'Y' or answer == ' ':
        return True
    else:
        return False


def usingAppsQuestion():
    '''ask user which apps to use'''
    print('Выберите используемые приложения:\nEnter = [y]')
    answers = []

    Chrome = input('Используем Chrome? ([y]/n):')
    answers.append(getAnswerBool(Chrome))

    Edge = input('Используем Edge? ([y]/n):')
    answers.append(getAnswerBool(Edge))

    Yandex = input('Используем Yandex? ([y]/n):')
    answers.append(getAnswerBool(Yandex))

    #Teams = input('Используем Teams? ([y]/n):')
    #answers.append(getAnswerBool(Teams))

    return answers


def getUsingAppsSettings():
    '''get settings from yaml file'''
    try:
        with open('userData/settings.yaml', 'r') as file:
            settings = yaml.full_load(file)

    except FileNotFoundError:
        with open('userData/settings.yaml', 'w') as file:
            isUsing = usingAppsQuestion()
            file.write(
                f'Google: {isUsing[0]}\nEdge: {isUsing[1]}\nYandex: {isUsing[2]}\nTeams: {isUsing[3]}')
            file.close()
            settings = yaml.full_load(file)
    return settings


def calculateWindows(usingApps):
    return usingApps.count(True)


def whichAppsLaunch(appsSettings=getUsingAppsSettings()):
    '''return list of apps to launch'''
    apps = list()
    if appsSettings['Google']:
        apps.append('Chrome')
    if appsSettings['Edge']:
        apps.append('Edge')
    if appsSettings['Yandex']:
        apps.append('Yandex')
    if appsSettings['Teams']:
        apps.append('Teams')
    return apps


def checkForTeamsApp(usingApps):
    '''check if Teams app is used'''
    if 'Teams' in usingApps:
        return True
    else:
        return False


def getBoxes():
    if len(whichAppsLaunch()) == 1:
        return fullscreen
    elif len(whichAppsLaunch()) == 2:
        return splitscreenLeft, splitscreenRight
    elif len(whichAppsLaunch()) == 3:
        return leftUpBox, rightUpBox, leftDownBox
    elif len(whichAppsLaunch()) == 4:
        return leftUpBox, rightUpBox, leftDownBox, rightDownBox
