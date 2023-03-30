from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
import time
import threading

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)

def skipTwo():
    pressTab()
    pressTab()

def on_press(key):
    global paused
    if "shift" in str(key):
        paused = not paused

def main():        
    print("Click on the first field")
    time.sleep(5)
    while(True):
        for i in range(14):
            if not paused:
                keyboard.type('ex')
                time.sleep(2)
                pressTab()

        if not paused:
            keyboard.type('Very good')
            skipTwo()


paused = True
thread = threading.Thread(target=main)
thread.start()

with Listener(on_press = on_press) as listener:
    listener.join()