# import win32api

# print(win32api.ShellExecute(1, 'open',
#  r'C:\Program Files (x86)\Tencent\QQPlayer\QQPlayer.exe',
#  '', '', 1))

import time
import win32api
import win32gui,win32con

print(win32api.GetCursorPos())
win32api.SetCursorPos((100,100))

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 100, 100, 0, 0)
time.sleep(2)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 100, 100, 0, 0)
# win32api.MessageBox(0,"Hello dd","MessageBox",win32con.MB_OK|win32con.MB_ICONWARNING)
# x = win32gui.FindWindow(None,"newText - 记事本")
# print(x)

# print(win32gui.GetClassName(7276358))



# hwndList = []

# win32gui.EnumWindows(lambda hWnd,param:param.append(hWnd),hwndList)

# for hwnd in hwndList:
#     title = win32gui.GetWindowText(hwnd)
#     print(title)
