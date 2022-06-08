import target_health
import random
import time
import pyautogui

def choose():
    target = None
    target1, target2 = target_health.target_health()
    if target1 < 25 and target2 < 25:
        time.sleep(random.randint(0,15))
    elif target1 < 25:
        target = "target2"
    elif target2 < 25:
        target = "target1"
    return target

def attack():
    target = choose()
    if target is not None:
        if target == "target1":
            pyautogui.click(1820, 478)
        elif target == "target2":
            pyautogui.click(1820, 500)

