Это простой кликер для Raid Shadows Legends.

Что он делает?
Просто кликает по очереди 10 команд и играет ровно 1 бой.
Задержка между боями по умолчанию между боями 60 секунд, Вы можете отредактировать ее в любую сторону.
time.sleep(60)

Для запуска кликера, Вам нужно будет также узнать координаты и отредактировать их:
# List of coordinates to click initially
INITIAL_COORDINATES = [(1149, 288), (1167, 382), (1155, 484), (1141, 596), (1148, 699), (1154, 817), (1149, 919), (1139, 1023), (1149, 1135), (1163, 1239)]

# Coordinate for intermediate clicks
INTERMEDIATE_COORDINATE = (1154, 1306)

# Coordinate for repeated clicks
REPEAT_COORDINATE = (764, 1305)

Чтобы узнать свои координаты запустите сначала скрипт mouse.py
Разумеется для начала у Вас должен быть установлен python в зависимости от версии python и окружения команда может быть:
pythin2 arena.py
pythin3 arena.py
py arena.py

Также Вам надо будет поставить несколько библитек, через pip
pip3 install time
pip3 install pyautogui