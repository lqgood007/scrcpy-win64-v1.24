import keyboard
import time
import subprocess
import adbUtil


t_fps = 1/30
t = time.time()
class Key_Manager():
    def __init__(self,device_list):
        self.key_pool = set()
        self.device_list = device_list
    def key_callback(self,code):
        if time.time()-t<t_fps:
            return

        if code.event_type == 'down':
            self.key_pool.add(code.name)
        if code.event_type == "up":
            if self.key_pool.__contains__(code.name):
                self.key_pool.remove(code.name)

        if 'a' in self.key_pool and 's' in self.key_pool:
            print('as')
        if 'a' in self.key_pool and 'w' in self.key_pool:
            print('aw')
        if 'w' in self.key_pool and 's' in self.key_pool:
            print('ws')
        if 'w' in self.key_pool and 'd' in self.key_pool:
            print('wd')
        if 'a' in self.key_pool:
            print('a')
        if 's' in self.key_pool:
            print('s')
        if 'd' in self.key_pool:
            print('d')
        if 'w' in self.key_pool:
            print('w')
        if 'q' in self.key_pool:
            print('q')
        if 'f' in self.key_pool:
            print('f')
        if 'j' in self.key_pool:
            print('j')
        if '1' in self.key_pool:
            print('1')
        if '2' in self.key_pool:
            print('2')
        if '3' in self.key_pool:
            print('3')
        if '4' in self.key_pool:
            print('4')

        if 'esc' in self.key_pool:
            print('esc')

    def tap_func(self,x,y):
        for i in self.device_list:
            s = subprocess.Popen("adb shell -s {} input tap {} {}".format(i,x, y))

    def swipe_func(self,x,y):
        for i in self.device_list:
            s = subprocess.Popen("adb shell -s {} input swipe {} {} 200".format(i,x, y))


if __name__ == '__main__':
    device_list = adbUtil.GetDevicesList()
    adbUtil.Boot_Grid_AndroidScreen(device_list)
    time.sleep(5)
    km = Key_Manager(device_list)

    keyboard.hook(lambda e: km.key_callback(e))

