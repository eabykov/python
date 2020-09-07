import pyautogui as auto
import keyboard as key

start_key = input( "Клавиша запуска: " )
stop_key = input( "Клавиша остановки: " )

def start():
    while True:
        input("Press {0} to start...".format(start_key))

def stop():
    while True:
        input("Press {0} to stop...".format(stop_key))

while True:
    if key.is_pressed( start_key ):
        auto.click(clicks=2, interval=0.25)
        if key.is_pressed( stop_key ):
            break