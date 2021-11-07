from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#X:  862 Y:  615 RGB: (177, 181, 234)
#X:  750 Y:  616 RGB: (255, 255, 255)
#X:  644 Y:  620 RGB: (128, 130, 153)
#X:  524 Y:  614 RGB: (159, 164, 231)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(838, 610)[0] == 0:
        click(838, 610)
    if pyautogui.pixel(729, 610)[0] == 0:
        click(729, 610)
    if pyautogui.pixel(640, 610)[0] == 0:
        click(640, 610)
    if pyautogui.pixel(516, 610)[0] == 0:
        click(516, 610)   
