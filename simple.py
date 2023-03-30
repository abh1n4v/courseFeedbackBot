from pynput.keyboard import Key, Controller
from pynput import keyboard
import random
import time

keyboard = Controller()

def pressTab(n):
    for i in range(n):
        keyboard.tap(Key.tab)
        time.sleep(0.1)

def randomizer():
    random_list = ['ex','ve']
    return random.choice(random_list)

def fill(n,m):
    for i in range(n):
        for _ in range (m):
            keyboard.type(randomizer())
            time.sleep(2)
            pressTab(1)
        keyboard.type('Good class')
        pressTab(2)

def main():        
    t = int(input("Enter number of Theory Courses: "))
    p = int(input("Enter number of Practical Courses: "))

    print("Click on the first field within 10 seconds")
    time.sleep(10)
    while(True):
        fill(t,14)
        pressTab(1)
        fill(p,13)
        print("Script Stopped")
        break

main()
