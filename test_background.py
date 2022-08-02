import os
import time
import pyautogui
import cv2
import numpy as np
import time
import win32gui
import win32con
import win32api


def doClick(cx, cy,hwnd):
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


h = win32gui.FindWindow(None, "R5CN710WMYD")
h = 13046586
# for i in range(100):
#         time.sleep(0.05)
#         win32api.keybd_event(13, 0, 0, 0)
#         win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.3)
win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.1)
win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.3)
win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.1)
win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.3)
win32api.SendMessage(h, win32con.WM_IME_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
time.sleep(0.1)
# doClick(100,100,h)
# doClick(100,100,h)
#
# win32api.SendMessage(h, win32con.WM_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
# time.sleep(0.1)
# win32api.SendMessage(h, win32con.WM_KEYUP, win32con.VK_SPACE, None)  # 模拟鼠标按下
# time.sleep(0.1)
# win32api.SendMessage(h, win32con.WM_KEYDOWN, win32con.VK_SPACE, None)  # 模拟鼠标按下
# time.sleep(0.1)
# win32api.SendMessage(h, win32con.WM_KEYUP, win32con.VK_SPACE, None)  # 模拟鼠标按下
# time.sleep(0.1)
# win32api.SetCursorPos([100, 100])
# #根据横纵坐标定位光标
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# #给光标定位的位置进行单击操作（若想进行双击操作，可以延时几毫秒再点击一次）
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
# #给光标定位的位置进行右击操作

# doClick(100,100,h)
# doClick(100,100,h)

#
#
# win32api.SendMessage(h, win32con.VK_SPACE, win32con.VK_SPACE, 0)
# time.sleep(1)
# win32api.SendMessage(h, win32con.VK_SPACE, win32con.VK_SPACE, 0)
# win32api.SendMessage(h, win32con.VK_SPACE, win32con.VK_SPACE, 0)
