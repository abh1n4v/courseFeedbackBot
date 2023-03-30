from pynput.keyboard import Key, Controller
from pynput import keyboard
import ast
import time

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)


def skipTwo():
    pressTab()
    pressTab()

def fill_feedback():
    for i in range(14):
        keyboard.type('ex')
        time.sleep(1.5)
        pressTab()

    keyboard.type('Very good')
    skipTwo()
    
print("Click on the first field")
time.sleep(5)

def main():
    while(True):
        fill_feedback()

main()