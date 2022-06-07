from PIL import Image
from pyautogui import *
import get_screen

dir = "C:\\Users\Marcin\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"
screen = get_screen.get_latest_image(dir)

im = Image.open(screen).convert("RGB")
target1, target2 = (1772, 478, 1900, 479), (1772, 500, 1900, 501)
box1, box2 =  im.crop(target1), im.crop(target2)
width1, width2 = box1.size[0], box2.size[0]
height1, height2 = box1.size[1], box2.size[1]
pix1, pix2 = box1.load(), box2.load()
missing_health1, missing_health2 = 0, 0
for i in range(width1):
    for j in range(height1):
        r,g,b = pix1[i, j]
        if r in (range(1, 85)):
            missing_health1 += 1

health1 = 128 - missing_health1
h1pct = health1*100/128

for l in range(width2):
    for m in range(height2):
        r,g,b = pix2[l, m]
        if r in (range(1, 85)):
            missing_health2 += 1

health2 = 128 - missing_health2
h2pct = health2*100/128

print(h1pct)
print(h2pct)

box1.show()
box2.show()
