# Flash ALL built in LED random colours
# random interval 0 - 0.5 seconds between each set colours
import time
import board
from random import randint, uniform
import neopixel
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.02)
while True:
    for Loop in range(10):
        np[Loop] = (randint(0, 255), randint(0, 255), randint(0, 255))
    np.show()
    time.sleep(uniform(0, 0.5))
