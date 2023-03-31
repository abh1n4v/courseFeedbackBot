from pynput.keyboard import Key, Controller
from pynput import keyboard
import random
import time

keyboard = Controller()

def pressTab(n):
    for i in range(n):
        keyboard.tap(Key.tab)
        time.sleep(0.1)
# to select random options between Excellent and VeryGood. 
def randomizer():
    random_list = ['ex','ex','ex','ve','ve','go']
    return random.choice(random_list)
#function to fill option on the site.
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
   # To give a pause of 10sec to switch from program to chrome tab.
    time.sleep(10)
    while(True):
        fill(t,14)
        pressTab(1)
        fill(p,13)
        print("Script Stopped")
        break

main()
