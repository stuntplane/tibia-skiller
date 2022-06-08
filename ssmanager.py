import pyautogui
import os
import glob

def delSS(dir):
    files = glob.glob(dir + ".*")
    for f in files:
        os.remove(f)

def makeSS(dir):
    path = os.lastdir(dir)
    if len(path) == 0:
        pyautogui.press("num*")