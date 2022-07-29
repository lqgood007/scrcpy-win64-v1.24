import os
import time
import pyautogui
import cv2
import numpy as np
import time
import win32gui
import win32con

class CV():
    def __init__(self):
        print('init CV')

    def get_rect_img(self,rect):##30fps
        img = pyautogui.screenshot(region=rect)
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        return img

    def check_engery(self):
        pass

    def check_bag_full(self):
        pass

    def check_mission_hand(self):
        pass

    def check_mission_going(self):
        pass

    def check_enter_under_button(self):
        pass

    def get_player_position(self):
        pass

    """
    battle check npc battle_over itempick map_arrow battle_arrow
    """
    def check_close_button(self):
        pass

    def check_mission_passed(self):
        pass

    def check_award_pick(self):
        pass

    def check_repair(self):
        pass

    def check_disassemble(self):
        pass

    def check_next_mission(self):
        pass

    def check_next_mission_button(self):
        pass

class GameStage():
    def __init__(self):
        print('init GameStage')
        self.player_stage = ['1','2','3','4','5']
        self.game_stage = ['town','underground','ui','switch_player']

class InputManager():
    def __init__(self):
        pass

    def point_random(self):
        pass




if __name__ == '__main__':
    s = os.popen("adb devices")
    a = s.read()
    list = a.split('\n')
    deviceList = []
    for temp in list:
        if len(temp.split()) > 1:
            if temp.split()[1] == 'device':
                deviceList.append(temp.split()[0])
    command = ""
    print('本次共扫描出%s' % (deviceList))

    window_dic = {}
    screen_count = 0
    screen_height = 960
    app_x = 0
    app_y = 0
    for device in deviceList:
        print("%s的投屏"%device)
        command = "scrcpy -m {} --power-off-on-close -w --window-borderless --window-title {} --bit-rate 4M -S -s {}".format(screen_height, device, device)
        # command = "scrcpy -m {} --power-off-on-close -w --window-title {} --bit-rate 4M -S -s {}".format(screen_height, device, device)
        t = os.popen(command)
        time.sleep(2)
        h = win32gui.FindWindow(None, device)
        rect = win32gui.GetWindowRect(h)
        app_x = rect[2]-rect[0]
        app_y = rect[3]-rect[1]
        screen_id = (screen_count // ((1920//app_y)*(1080//app_x)))
        screen_xcoor = (screen_count % (1920//app_y))*app_y+ 1920*screen_id
        screen_ycoor = (screen_count % ((1920//app_y)*(1080//app_x))) // (1920//app_y)*app_x
        win32gui.SetWindowPos(h, win32con.HWND_TOPMOST, screen_xcoor, screen_ycoor, rect[2] - rect[0], rect[3] - rect[1],
                              win32con.SWP_SHOWWINDOW)
        window_dic[device] = {'pid':h}

        screen_count+=1
    print(window_dic)
    print(app_x,app_y)
    i = 0
    screen_CV = CV()

    t = time.time()
    h = win32gui.FindWindow(None, deviceList[0])
    rect = win32gui.GetWindowRect(h)

    exit()