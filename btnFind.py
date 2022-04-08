import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui as pag

import cv2

kWidth = 1920/pag.size()[0]  # опитимизация под разные разрешения
kHeight = 1080/pag.size()[1]
# регионы для поиска кнопок на экране pyautogui
upperBox = [0, 0, int(1920*kWidth), 360]
lowerBox = [0, int(kHeight*600), int(1920*kWidth), 380]
midBox = [0, int(kHeight*350), int(1920*kWidth), 350]
logoBox = [0, 0, int(kHeight*250), int(kWidth*150)]


# function to find the button on the screen
def getImageCoordinatesOnScreenshot(img, box, gray=True):
    try:
        return pag.locateCenterOnScreen(img, region=box, grayscale=gray, confidence=0.9)
    except Exception as e:
        print(e, 'Error in getImageCoordinatesOnScreenshot()')
        return False


def clickOnButton(img, box):
    x, y = getImageCoordinatesOnScreenshot(
        img, box)
    pag.moveTo(x, y)
    time.sleep(0.1)
    pag.click()


def findPattern():
    if(getImageCoordinatesOnScreenshot('assets/darkPattern.png', midBox, False)):
        return 'Dark'
    else:
        return 'Light'


def findLogo():
    if(getImageCoordinatesOnScreenshot('assets/teamsLogoLight.png', upperBox, False)):
        return 'Light'
    elif(getImageCoordinatesOnScreenshot('assets/teamsLogoDark.png', upperBox, False)):
        return 'Dark'
    # в случае если скипаем "использовать веб-приложение" получаем тему из фона
    elif (getImageCoordinatesOnScreenshot('assets/teamsLogoJoined.png', logoBox, False)):
        return findPattern()
    else:
        return 'Error'


def pressConnectButton():
    flag = True
    time.sleep(2)
    while(flag):
        try:
            clickOnButton('assets/buttons/connect.png', lowerBox)
            flag = False
        except:
            time.sleep(0.5)
            print('Не найдена кнопка подключения')


def pressContinueButton():
    flag = True
    while(flag):
        try:
            clickOnButton('assets/buttons/continueNosound.png',
                          lowerBox)
            flag = False
        except:
            time.sleep(0.5)
            print('Не найдена кнопка продолжения')


def pressConnectnowButton():
    flag = True
    while(flag):
        try:
            clickOnButton('assets/buttons/connectnow.png', midBox)
            flag = False
        except:
            time.sleep(0.5)
            print('Не найдена кнопка подключения')


def pressButtonsForConnect(Logo):
    # универсализация под светлую\темную тему
    if (Logo == 'Light'):
        try:
            clickOnButton('assets/buttons/useWebAppLight.png', lowerBox)
        except Exception as e:
            print(e, 'Error in pressButtonsForConnect() in case of Light theme')
        finally:
            pass
    elif(Logo == 'Dark'):
        try:
            clickOnButton('assets/buttons/useWebAppDark.png', lowerBox)
        except Exception as e:
            print(e, 'Error in pressButtonsForConnect() in case of Dark theme')
        finally:
            pass
    pressConnectButton()
    pressContinueButton()
    pressConnectnowButton()


def pressCancelButton():
    try:
        clickOnButton('assets/buttons/cancelGoogle.png', upperBox)
    except:
        pass
    try:
        clickOnButton('assets/buttons/cancelEdge.png', upperBox)
    except:
        pass
    try:
        clickOnButton('assets/buttons/cancelYandex.png', upperBox)
    except:
        pass


def scriptBrowser():
    while (findLogo() == 'Error'):
        time.sleep(0.5)
    Logo = findLogo()
    # нажатие на "отмена" при предложении перейти в приложение
    pressCancelButton()
    pressButtonsForConnect(Logo)
