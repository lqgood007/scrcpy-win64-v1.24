import win32gui
import win32con
windows_list = []

title = "R5CN710WMYD"
h = win32gui.FindWindow(None,title)
rect = win32gui.GetWindowRect(h)
win32gui.SetWindowPos(h,win32con.HWND_TOPMOST,-500,0,rect[2]-rect[0],rect[3]-rect[1],win32con.SWP_SHOWWINDOW)