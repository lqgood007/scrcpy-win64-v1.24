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
    if code.name == 'j' and code.event_type == 'down':
        x,y = 1117,554
        t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    """
    1/2/3/4 技能
    """
    if code.name == '1' and code.event_type == 'down':
        x,y = 1117,554
        t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    if code.name == '2' and code.event_type == 'down':
        x,y = 1117,554
        t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    if code.name == '3' and code.event_type == 'down':
        x,y = 1117,554
        t = subprocess.Popen("adb shell input tap {} {}".format(x,y))
    if code.name == '4' and code.event_type == 'down':
        x,y = 1117,554
        t = subprocess.Popen("adb shell input tap {} {}".format(x,y))




    print(code.name, code.event_type)





if __name__ == '__main__':
    keyboard.hook(lambda e: check_key_code(e))
    keyboard.wait('Ctrl')