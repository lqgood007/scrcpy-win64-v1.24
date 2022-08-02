import keyboard
import time
import subprocess
down_key_list = []

subprocess_dic = {}
click_tick = 0.05
click_timer = {}

def check_key_code(code):
    """
    attack-j
    """
    print(code.name, code.event_type)

    # if code.name == 'j' and code.event_type == 'down':
    #     x,y = 1117,554
    #     t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    # """
    # 1/2/3/4 技能
    # """
    # if code.name == '1' and code.event_type == 'down':
    #     x,y = 1117,554
    #     t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    # if code.name == '2' and code.event_type == 'down':
    #     x,y = 1117,554
    #     t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    # if code.name == '3' and code.event_type == 'down':
    #     x,y = 1117,554
    #     t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    # if code.name == '4' and code.event_type == 'down':
    #     x,y = 1117,554
    #     t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
t_fps = 1/30
t = time.time()
class Key_Manager():
    def __init__(self):
        self.key_pool = set()
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
        if 'q' in self.key_pool:
            print('a')
        if 'q' in self.key_pool:
            print('s')
        if 'q' in self.key_pool:
            print('d')
        if 'q' in self.key_pool:
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
        s = subprocess.Popen("adb shell input tap {} {}".format(x, y))




class A():
    def __init__(self):
        self.Global_p1= 0
    def keytest(self):
        self.Global_p1+=1


if __name__ == '__main__':
    km = Key_Manager()
    keyboard.hook(lambda e: km.key_callback(e))
    keyboard.wait('Ctrl')

