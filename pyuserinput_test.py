import win32api, win32con, time, cv2,win32gui,os,sys,numpy as np,win32ui
from PIL import Image, ImageGrab

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
import lunia.pictool as lp, lunia.constant as lc,lunia.luniatool as lt,lunia.numberpictool as ln

class LuniaGameWindows:
    def __init__(self):
        self.windowTitle = lc.gameWindowTitle
        self.wds=[]
        self.wdposes=[]
        win32gui.EnumWindows(self.findLuniaWindows, 0)
        self.sortWindows()

    def findLuniaWindows(self,x,mouse):
        if win32gui.GetWindowText(x)==self.windowTitle:
            self.wds.append(x)
            self.wdposes.append(win32gui.GetWindowRect(x))

    # 第i窗口截图
    def captureWindow(self,i,offset1=None,offset2=None,doActive=False,use_offset=True):
        if doActive:
            time.sleep(.5)
            win32gui.SetForegroundWindow(self.wds[i])
            time.sleep(1)
        if use_offset:
            # 对 距离第i个窗口的左上角 offset1和offset2 的内部矩形 截图
            return self.capture(*self.calculatePos(i,offset1),*self.calculatePos(i,offset2))
        else:
            return self.capture(*offset1, *offset2)             # 直接按坐标截图

    def capture(self,x1, y1, x2, y2):
        img = ImageGrab.grab((x1, y1, x2, y2))
        return img

    def calculatePos(self,i,offset):
        return self.wdposes[i][0] + offset[0],  self.wdposes[i][1] + offset[1]

    def sortWindows(self):
        self.wds=[x for y, x in sorted(zip(self.wdposes,self.wds),key=lambda x:x[0][0])]
        self.wdposes=sorted(self.wdposes,key=lambda x:x[0])
        print('窗口句柄是{}'.format(self.wds))
        print('窗口坐标是{}'.format(self.wdposes))

    # 对后台窗口键盘/鼠标输入，对一些程序部分按键无效，原因不明
    def doClick(self,hwnd,cx, cy):
        time.sleep(1)
        print(hwnd,cx, cy)
        pos = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
        # win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, pos)
        time.sleep(2)
        i=win32con.VK_ESCAPE
        i=98
        win32api.PostMessage(hwnd, win32con.WM_RBUTTONDOWN, 0,0)  # 模拟鼠标按下
        win32api.PostMessage(hwnd, win32con.WM_RBUTTONUP, 0,0)  # 模拟鼠标弹起
        time.sleep(2)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN,i,0)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, i, 0)

    def capture_background(self,i):
        hWnd=self.wds[i]
        # 获取句柄窗口的大小信息
        left, top, right, bot = self.wdposes[i]
        width = right - left
        height = bot - top
        # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
        hWndDC = win32gui.GetWindowDC(hWnd)
        # 创建设备描述表
        mfcDC = win32ui.CreateDCFromHandle(hWndDC)
        # 创建内存设备描述表
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建位图对象准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 为bitmap开辟存储空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        # 将截图保存到saveBitMap中
        saveDC.SelectObject(saveBitMap)
        # 保存bitmap到内存设备描述表
        saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im_PIL = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

        # 内存释放
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hWnd, hWndDC)

        im_PIL.show()  # 显示




if __name__=='__main__':
    lgw=LuniaGameWindows()
    i=-1
    hwnd=lgw.wds[i]
    # lgw.doClick(hwnd, 620, 580)
    lgw.capture_background(-1)
    # img=lgw.captureWindow(i,lgw.wdposes[i][:2],lgw.wdposes[i][2:],doActive=True,use_offset=False)
    # img.show()
    # src = np.array(img, np.uint8).reshape(img.size[1], img.size[0], -1)
