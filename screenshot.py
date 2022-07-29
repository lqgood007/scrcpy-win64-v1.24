import pyautogui
import cv2
import numpy as np
import time
t = time.time()
img = pyautogui.screenshot(region=[0,0, 400, 600])  # 分别代表：左上角坐标，宽高
print(time.time()-t)
#对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
#因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
time_tag = time.time()
i = 0
while i<=1000:
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    i+=1
print(time.time()-time_tag)
cv2.imshow("截屏",img)
cv2.waitKey(0)
