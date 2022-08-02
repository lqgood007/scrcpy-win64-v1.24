import subprocess
import time

x,y = 1117,554
t = 0.1
tt = time.time()
while True:
    if time.time()-tt > t:
        s = subprocess.Popen("adb shell input tap {} {}".format(x,y))
        time.sleep(0.3)
        s = subprocess.Popen("adb shell input tap {} {}".format(1074,419))
        time.sleep(0.2)
        s = subprocess.Popen("adb shell input tap {} {}".format(986,504))
        time.sleep(0.2)
        s = subprocess.Popen("adb shell input tap {} {}".format(933,370))
        time.sleep(0.3)

        tt = time.time()
