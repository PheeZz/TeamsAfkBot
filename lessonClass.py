import dateAndTime as dt
import btnFind as btn
import webbrowser as webbr
import time
import pyautogui as pag
from random import randint
import pygetwindow as gw
from btnFind import scriptBrowser
from windowsCalculator import whichAppsLaunch


def waitForOpenApps():
    while(len(gw.getWindowsWithTitle('Microsoft Teams')) != len(whichAppsLaunch())):
        time.sleep(1)


def waitForOpenOneApp(app):
    while(len(gw.getWindowsWithTitle(app)) != 1):
        time.sleep(0.5)


def resizeWindow(browser, box):
    '''
    resize window\n
    box - list to set window size as ['x','y','width','height']\n
    window - window name\n
    '''
    if browser == 'Yandex':
        browser = 'Яндекс.Браузер'
    try:
        waitForOpenOneApp(browser)
        window = gw.getWindowsWithTitle('Microsoft Teams' and browser)[0]
        window.resizeTo(box[2], box[3])
        window.moveTo(box[0], box[1])
    except Exception as error:
        print(
            f'Ошибка при изменении размера окна {browser}: {error}')
    finally:
        print(
            f'{browser} resized to {box[2]}x{box[3]} and moved to {box[0]}x{box[1]}')


def openLessonBrowser(browser, link):
    '''
    browser - browser name\n
    link - link to open\n
    '''
    webbr.get(browser).open_new_tab(link)


def localizeToRU(browser):
    if browser == 'Yandex':
        return 'Microsoft Teams — Yandex'
    elif browser == 'Chrome':
        return 'Microsoft Teams — Google Chrome'
    elif browser == 'Edge':
        return 'Microsoft Teams — Личный: Microsoft\u200b Edge'


class Lesson():
    def __init__(self, link='', endTime='', name='', browser='', box=list(0 for x in range(4))):
        '''constructor'''
        self.link = link
        self.endTime = endTime
        self.name = name
        self.browser = browser
        self.box = box

    def __str__(self):
        '''return lesson info'''
        return f"Пара: {self.name}\nСсылка: {self.link}\nВремя окончания: {self.endTime}\nИспользуемое приложение: {self.browser}\nКоординаты и размер окна: {self.box}\n"

    def getLessonInfoFromShedule(self, shedule, time):
        '''construct lesson object from shedule.yml'''
        today = dt.updateToday()
        self.link = shedule[today][time]['link']
        self.endTime = dt.endTime(time)
        self.name = shedule[today][time]['lesson']

    def setBox(self, box):
        self.box = box

    def getEndtime(self):
        return self.endTime

    def sleep(self):
        '''sleep until lesson endTime'''
        flag = True
        while(flag):
            # защита от дебила, чтобы все одновременно не ливали с пары
            if self.endTime <= dt.nowToDatetime():
                time.sleep(10+randint(0, 5))
                pag.click(self.box[0]+self.box[2]/2,
                          self.box[1]+self.box[3]/2)
                gw.getActiveWindow().close()
                flag = False
            else:
                time.sleep(30)

    def launch(self):
        '''function for launching lesson'''
        openLessonBrowser(self.browser, self.link)

        '''
        пока писал забыл зачем мне эта регулярка :'(
        windowsTitleList = list()
        for i in range(len(gw.getAllTitles())):
            if (re.search(r'Microsoft Teams', gw.getAllTitles()[i])) is not '':
                try:
                    windowsTitleList.append(
                        (re.search(r'Microsoft Teams(\s*\S){,100}', gw.getAllTitles()[i])).group())
                except:
                    pass
        '''

        resizeWindow(self.browser, self.box)

    def connect(self):
        scriptBrowser(self.box)

    def launchWithTeamsApp(self):
        '''function for launching lesson with browsers and\or teams app'''
        pass
