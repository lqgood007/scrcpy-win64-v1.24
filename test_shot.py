from __future__ import print_function

import os
import time
import pyautogui
import cv2
import numpy as np
import time
import win32gui
import win32con
from PIL import ImageGrab


from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)


def A():
    t = time.time()
    i = 0
    while i <1000:
        pyautogui.screenshot(region=[0,0,50,10])
        i+=1
    print(time.time()-t)

def B():
    t = time.time()
    i = 0
    while i < 1000:
        h = win32gui.FindWindow(None, "R5CN710WMYD")
        rect = win32gui.GetWindowRect(h)
        i += 1
    print(time.time()-t)

def C():
    t = time.time()
    i = 0
    while i <1000:
        img = ImageGrab.grab(bbox=(0,0,10,50))
        i+=1
    print(time.time()-t)

def D():
    t = time.time()
    i = 0
    while i <1000:
        # entireScreen = getScreenAsImage()
        entireScreen = getRectAsImage((0,0,50,10))
        i+=1
    print(time.time()-t)

if __name__ == '__main__':
    print('start')
    D()
    print('end')
