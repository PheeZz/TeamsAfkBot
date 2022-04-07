import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui as pag
import webbrowser as webbr
import cv2

kWidth = 1920/pag.size()[0]  # опитимизация под разные разрешения
kHeight = 1080/pag.size()[1]
# регионы для поиска кнопок на экране pyautogui
upperBox = [0, 0, 1920*kWidth, 360*kHeight]
lowerBox = [0, 600, 1920*kWidth, 380*kHeight]
logoBox = [0, 0, 250, 150]


# function to find the button on the screen
async def getImageCoordinatesOnScreenshot(img, box):
    try:
        return pag.locateCenterOnScreen(img, grayscale=True, region=box, confidence=0.8)
    except Exception as e:
        print(e)
        return False


def clickOnButton(img, box):
    pag.click(getImageCoordinatesOnScreenshot(
        img, box))


async def findLogo():
    if(getImageCoordinatesOnScreenshot('assets/teamsLogoLight.png', upperBox)):
        return 'Light'
    elif(getImageCoordinatesOnScreenshot('assets/teamsLogoDark.png', upperBox)):
        return 'Dark'
    else:
        return 'Error'


async def isExistTodayLabel():
    if(getImageCoordinatesOnScreenshot('assets/todayLabelDark.png', lowerBox)):
        return True
    elif(getImageCoordinatesOnScreenshot('assets/todayLabelLight.png', lowerBox)):
        return True
    else:
        return False


async def isExistConnectButton():
    if(getImageCoordinatesOnScreenshot('assets/buttons/connectButton.png', lowerBox)):
        return True
    else:
        return False


async def isExistContinueButton():
    if(getImageCoordinatesOnScreenshot('assets/buttons/continueWOsoundAndVic.png', lowerBox)):
        return True
    else:
        return False


def pressButtonsForConnect(Logo):
    # универсализация под светлую\темную тему
    if (Logo == 'Light'):
        try:
            clickOnButton('assets/buttons/useWebAppLight.png', lowerBox)
        except Exception as e:
            print(e)
    elif(Logo == 'Dark'):
        try:
            clickOnButton('assets/buttons/useWebAppDark.png', lowerBox)
        except Exception as e:
            print(e)
    while (isExistTodayLabel() == False):
        time.sleep(0.5)
    while(isExistConnectButton() == False):
        time.sleep(0.5)
    clickOnButton('assets/buttons/connectButton.png', lowerBox)
    while(isExistContinueButton() == False):
        time.sleep(0.5)
    clickOnButton('assets/buttons/continueWOsoundAndVic.png', lowerBox)


def pressCancelButton():
    try:
        clickOnButton('assets/buttons/cancelGoogle.png', upperBox)
    except Exception as e:
        pass
    try:
        clickOnButton('assets/buttons/cancelEdge.png', upperBox)
    except Exception as e:
        pass
    try:
        clickOnButton('assets/buttons/cancelYandex.png', upperBox)
    except Exception as e:
        print(e)


async def scriptBrowser():
    while (findLogo() == 'Error'):
        time.sleep(0.5)
    Logo = findLogo()
    # нажатие на "отмена" при предложении перейти в приложение
    pressCancelButton()
    pressButtonsForConnect(Logo)
