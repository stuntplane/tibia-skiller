import target_health
import Target
import time
import random

dir = "C:\\Users\Marcin\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"
try:
    while True:
        target_health.target_health(dir)
        Target.choose()
        time.sleep(random.randint(0,2))
        Target.attack()
except KeyboardInterrupt:
    pass