import os
import pyautogui
import cv2
import numpy as np
import time
import win32gui
import win32con

def GetDevicesList():
    list = os.popen("adb devices").read().split('\n')
    deviceList = []
    for temp in list:
        if len(temp.split()) > 1:
            if temp.split()[1] == 'device':
                deviceList.append(temp.split()[0])
    print('本次共扫描出 {} 个设备 ：{} '.format(len(deviceList),deviceList))
    return deviceList

def Boot_Grid_AndroidScreen(deviceList):
    window_dic = {}
    Screen_Height = 960
    screen_count = 0
    for device in deviceList:
        print("%s的投屏" % device)
        command = "scrcpy -m {} --power-off-on-close -w --window-borderless --window-title {} --bit-rate 4M -S -s {}".format(
            Screen_Height, device, device)
        t = os.popen(command)
        time.sleep(2)
        h = win32gui.FindWindow(None, device)
        rect = win32gui.GetWindowRect(h)
        app_x = rect[2] - rect[0]
        app_y = rect[3] - rect[1]
        screen_id = (screen_count // ((1920 // app_y) * (1080 // app_x)))
        screen_xcoor = (screen_count % (1920 // app_y)) * app_y + 1920 * screen_id
        screen_ycoor = (screen_count % ((1920 // app_y) * (1080 // app_x))) // (1920 // app_y) * app_x
        win32gui.SetWindowPos(h, win32con.TRANSPARENT, screen_xcoor - 1920, screen_ycoor, rect[2] - rect[0],
                              rect[3] - rect[1],
                              win32con.SWP_SHOWWINDOW)
        # window_dic[device] = {'pid': h}
        screen_count += 1

def swap_test():
    pass


if __name__ == '__main__':
    # print(GetDevicesList())
    Boot_Grid_AndroidScreen(GetDevicesList())
    swap_test()




"""
adb shell pm list packages -3  查看三方应用


adb shell am start com.netease.g67/com.netease.game.MessiahNativeActivity            启动暗黑

adb shell am force-stop com.netease.g67

adb shell input keyboard text "abc"  模拟输入


adb shell input tap 500 500  模拟点击

adb shell input swipe 500 300 400 300  模拟滑动  （x,y）->(x,y)

adb shell input swipe 500 300 100 300 500
adb shell input swipe 100 300 100 300 50000

adb shell input tap 600 800

"""