# RU

## на данный момент проверена работа только с темной темой teams, браузерами: Google Chrome, Yandex Browser, MS Edge

## Как скачать?
Лучший вариант - заглянуть в блок *Release* справа, но если же ты рискованный - можешь качать проект прямо с main ветки :) 
P.s я бы все таки рекомендовал качать релиз

## Если необходимо - смените ссылку на файл с расписанием в файле /userData/pastebin.txt

## Как работает этот бот?

 1. Происходит парсинг расписания с pastebin
 2. Устанавливается путь до исполняемого файла браузера (на данный момент доступен только *Google Chrome*)
 3. При соответсвии **текущей** даты\времени с датой\временем **начала** пары открывается команда в браузере
 4. С помощью компьютерного зрения выполняется поиск необходимых кнопок для "входа"
 5. Выполняется последовательный скрипт по нажатию необходимых кнопок
 6. В тайминг конца пары **вкладка** с лекцией закрывается
 7. Бот возвращается к пункту *3.*

## Как запустить бота?
Есть два варианта:

 1. Установить необходимые библиотеки и запустить файл main.py<br/>
`pip install pyautogui`<br/>
`pip install requests`<br/>
`pip install opencv-python`<br/>
`pip install pyYAML`<br/>
`pip install pygetwindow`<br/>

 2. Запустить TeamsAfkBot.exe в корневой папке, но в таком случае инициализация до запуска самого бота займет ~15 секунд (в зависимости hardware)

Если что то не работает:
 проверьте точно ли папка с ботом находится на одном диске с браузерами (windows - диск C)
 попробуйте запустить settings.exe, это перезапишет пути к браузерам

# EN

## How to download?
The best option is to look into the *Release* block on the right, but if you are risky, you can download the project directly from the main branch :)
P.s I would still recommend downloading the release

## If necessary, change the link to the file in the usual file /userData/pastebin.txt

## How does this bot work?

1. The schedule is parsed from pastebin
2. The path to the browser executable is set (only *Google Chrome* is available at the moment)
3. If the **current** date/time matches the date/time of the **beginning** of the pair, a command is opened in the browser
4. With the help of computer vision, the necessary buttons are searched for "input"
5. A sequential script is executed by pressing the necessary buttons
6. At the timing of the end of the pair, the **tab** with the lecture closes
7. The bot returns to point *3.*

## How to start the bot?
There are two options:

1. Install the required libraries and run the main.py file<br/>
`pip install pyautogui`<br/>
`pip install requests`<br/>
`pip install opencv-python`<br/>
`pip install pyYAML`<br/>
`pip install pygetwindow`<br/>

3. Run TeamsAfkBot.exe in the root folder, but in this case, initialization before starting the bot itself will take ~ 15 seconds (depending on hardware)
