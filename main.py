import os
import time

s=os.popen("adb devices")
a=s.read()
list=a.split('\n')
deviceList=[]
for temp in list:
    if len(temp.split())>1:
        if temp.split()[1]=='device':
            deviceList.append(temp.split()[0])
command=""
print('本次共扫描出%s'%(deviceList))

for device in deviceList:
    print("正在准备%s设备的投屏"%device)
    command = "scrcpy -m 960 -t --power-off-on-close -w --window-borderless --window-title {} --bit-rate 4M -S -s {}".format(device,device)

    # --window - borderless
    print(command)
    t = os.popen(command)
