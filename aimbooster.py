  
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 197)
lastclickx=0
lastclicky=0
screenx = 670
screeny = 340
count = 0
while keyboard.is_pressed('q') == False:
    
    pic = pyautogui.screenshot(region=(screenx,screeny,600,420))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            ##print(".",end="")
            r,g,b = pic.getpixel((x,y))
            if b == 197 and x != lastclickx and y != lastclicky:
                click(x+screenx,y+screeny)
                count+=1
                print("n°" + str(count) + "\t| " + str(x) + " " + str(y))
                lastclickx=x
                lastclicky=y
                ##time.sleep(0.05)
                break