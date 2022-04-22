import time
import pyautogui as pag
from windowsCalculator import *


# регионы для поиска кнопок на экране pyautogui

def moveToCenterOfBox(currentbox):
    pag.moveTo(currentbox[0]+currentbox[2]/2, currentbox[1]+currentbox[3]/2)

# function to find the button on the screen


def getImageCoordinatesOnScreenshot(img, box, gray=True):
    try:
        return pag.locateCenterOnScreen(img, region=box, grayscale=gray, confidence=0.9)
    except Exception as e:
        time.sleep(0.5)
        print(e, '\nError in getImageCoordinatesOnScreenshot()')
        return False


def waitGetAllConnectButtons(link):
    '''задержка для открытия всех окон'''
    while(len(list(pag.locateAllOnScreen('assets/buttons/connect.png', region=fullscreen, grayscale=True, confidence=0.9))) < len(whichAppsLaunch())):
        for opennedApp in whichAppsLaunch():
            if opennedApp == 'Yandex':
                check = 'Яндекс.Браузер'
            else:
                check = opennedApp
            if not pag.getWindowsWithTitle(check):
                openLessonBrowser(check, link)
        time.sleep(10)
        usingBoxlist = getBoxes()
        for box in usingBoxlist:
            pag.click(box[0]+box[2]/2, box[1]+box[3]/2)
            pag.hotkey('ctrl', 'r')


def clickOnButton(img, box):
    x, y = getImageCoordinatesOnScreenshot(
        img, box)
    pag.click(x, y)


def findPattern(currentBox):
    if pag.pixelMatchesColor(300+currentBox[0], 400+currentBox[1], (245, 245, 245), tolerance=30):
        return 'Light'
    elif pag.pixelMatchesColor(300+currentBox[0], 400+currentBox[1], (20, 20, 20), tolerance=30):
        return 'Dark'


def resetCoordinates(oldBox, newBox):
    oldBox[0] = newBox[0]  # start x coordinate
    oldBox[1] = newBox[1]  # start y coordinate
    oldBox[2] += newBox[2]  # end x coordinate
    oldBox[3] += newBox[3]  # end y coordinate
    return oldBox


def findLogo(currentBox):
    if(getImageCoordinatesOnScreenshot('assets/teamsLogoLight.png', resetCoordinates(upperBox, currentBox), False)):
        return 'Light'
    elif(getImageCoordinatesOnScreenshot('assets/teamsLogoDark.png', resetCoordinates(upperBox, currentBox), False)):
        return 'Dark'
    # в случае если скипаем "использовать веб-приложение" получаем тему из фона
    elif (getImageCoordinatesOnScreenshot('assets/teamsLogoJoined.png', resetCoordinates(logoBox, currentBox), False)):
        time.sleep(1)
        return findPattern(currentBox)
    else:
        return findPattern(currentBox)


def pressConnectButton(currentBox):
    flag = True

    while(flag):
        try:
            time.sleep(1)
            clickOnButton('assets/buttons/connect.png',
                          resetCoordinates(lowerBox, currentBox))
            flag = False
        except:
            print('Не найдена кнопка подключения1')
            moveToCenterOfBox(currentBox)
            pag.click()
            pag.hotkey('ctrl', 'r')  # refresh page after 5 seconds of waiting
            time.sleep(5)


def pressContinueButton(currentBox):
    flag = True
    while(flag):
        try:
            moveToCenterOfBox(currentBox)
            pag.click()
            pag.scroll(-2000)
            time.sleep(0.5)
            clickOnButton('assets/buttons/continueNosound.png',
                          resetCoordinates(lowerBox, currentBox))
            flag = False
        except:
            time.sleep(0.5)
            print('Не найдена кнопка продолжения')


def pressConnectnowButton(currentBox):
    flag = True
    while(flag):
        try:
            clickOnButton('assets/buttons/connectnow.png',
                          resetCoordinates(midBox, currentBox))
            flag = False
        except:
            print('Не найдена кнопка подключения2')
            time.sleep(0.5)


def pressButtonsForConnect(currentBox):
    # универсализация под светлую\темную тему

    pressConnectButton(currentBox)
    pressContinueButton(currentBox)
    pressConnectnowButton(currentBox)


def pressCancelButton(currentBox):
    try:
        clickOnButton('assets/buttons/cancelGoogle.png',
                      resetCoordinates(upperBox, currentBox))
    except:
        time.sleep(0.5)

    try:
        clickOnButton('assets/buttons/cancelEdge.png',
                      resetCoordinates(upperBox, currentBox))
    except:
        time.sleep(0.5)

    try:
        clickOnButton('assets/buttons/cancelYandex.png',
                      resetCoordinates(upperBox, currentBox))
    except:
        time.sleep(0.5)


def scriptBrowser(currentBox):
    while(findLogo(currentBox) == False):
        time.sleep(0.5)
        print('Не найден логотип')
    Theme = findPattern(currentBox)
    # нажатие на "отмена" при предложении перейти в приложение
    pressCancelButton(currentBox)
    pressButtonsForConnect(currentBox)
