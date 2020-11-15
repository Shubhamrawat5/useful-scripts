import keyboard
import time

time.sleep(2)

for i in range(22): #number of members count
    print(i)
    keyboard.press_and_release('shift+@')

    for j in range(i):
        keyboard.press_and_release('down')
    keyboard.press_and_release('enter')
    time.sleep(2)

