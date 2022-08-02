from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)  #高斯降噪，适度
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    #求梯度
    xgrd = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrd = cv.Sobel(gray,cv.CV_16SC1,0,1)

    egde_output = cv.Canny(xgrd,ygrd,50,150)  #50低阈值，150高阈值
    #egde_output = cv.Canny(gray,50,150)   #都可使用
    cv.imshow('canny_edge',egde_output)

    #输出彩色图
    dst = cv.bitwise_and(image,image,mask=egde_output)
    cv.imshow('color edge',dst)


if __name__ == "__main__":
    filepath = r"C:\Users\lee\Desktop\game\1.png"
    img = cv.imread(filepath)       # blue green red
    cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
    cv.imshow("input image",img)

    edge_demo(img)


    cv.waitKey(0)
    cv.destroyAllWindows()
