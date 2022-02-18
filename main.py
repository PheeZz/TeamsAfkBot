import pyscreenshot as ps
import numpy as np
import cv2  # работа с изображениями
import os  # запуск приложений
import webbrowser as webbr

tmpPath = open('google.txt')  # import app path from txt files
googlePath = tmpPath.read()
tmpPath = open('yandex.txt')
yandexPath = tmpPath.read()
tmpPath = open('msEdge.txt')
edgePath = tmpPath.read()
tmpPath = open('teamsApp.txt')
teamsAppPath = tmpPath.read()
print(googlePath, yandexPath, edgePath, teamsAppPath, sep='\n')

# os.startfile(googlePath)  # exec apps
# os.startfile(yandexPath)
# os.startfile(edgePath)
# os.startfile(teamsAppPath)            NOW DON'T NEED IT because realised by webbrowser lib

# register browsers names as path
webbr.register('Chrome', None, webbr.BackgroundBrowser(googlePath))
webbr.register('Yandex', None, webbr.BackgroundBrowser(yandexPath))
webbr.register('Edge', None, webbr.BackgroundBrowser(edgePath))

webbr.get('Chrome').open_new_tab('https://vk.com')
webbr.get('Yandex').open_new_tab('https://vk.com')
webbr.get('Edge').open_new_tab('https://vk.com')
