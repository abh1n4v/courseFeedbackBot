from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
import time
import threading

keyboard = Controller()

def pressTab(n):
    for i in range(n):
        keyboard.tap(Key.tab)

def on_press(key):
    global paused
    if "shift" in str(key):
        paused = not paused

def main():
    t = int(input("Enter number of Theory Courses: "))
    p = int(input("Enter number of Practical courses: "))
    print("Click on the first field and press Shift. Press Shift again to Interrupt.")
    time.sleep(10)
    for _ in range(t):
        for i in range(14):
            if not paused:
                keyboard.type('ex')
                time.sleep(2)
                pressTab(1)

        if not paused:
            keyboard.type('Very good')
            pressTab(2)
    
    if not paused:
        pressTab(1)

    for _ in range(p):
        for i in range(13):
            if not paused:
                keyboard.type('ex')
                time.sleep(2)
                pressTab(1)

        if not paused:
            keyboard.type('Very good')
            pressTab(2)

    print("Process Complete. You may close the terminal.")
    print("Star the repo if it helped ;)")
        
paused = True
thread = threading.Thread(target=main)
thread.start()

with Listener(on_press = on_press) as listener:
    listener.join()
