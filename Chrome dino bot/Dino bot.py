import pyautogui as py
from numpy import *
from PIL import ImageGrab, ImageOps
import time

time.sleep(3)
# py.write("Hello")
# py.mouseInfo()


def restart():
    py.click(480, 370)


def jump():
    py.keyDown("space")
    print("Jump")
    py.keyUp("space")

##adjust these x1,y1 and x2,y2 cordinates according next to dino area in box tupple. it will keep on reading that area and when something come then it will call jump function
def imagegrab():
    box = (260, 365, 344, 402) 
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    if int(a.sum()) != 3355:
        jump()


# BOX CORDINATES
# top = 770,350
# bottom = 860,400
# dino = 609,880
# bot_area = (770, 350, 860, 270)

restart()

while True:
    imagegrab()
