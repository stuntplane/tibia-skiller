import target_health
import Target
import time
import random
import ssmanager

dir = "C:\\Users\Marcin\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"
try:
    while True:
        ssmanager.makeSS(dir)
        target_health.target_health(dir)
        Target.choose()
        time.sleep(random.randint(0,2))
        Target.attack()
        ssmanager.delSS(dir)
except KeyboardInterrupt:
    pass