# Flashes All built in LED same random colours
# Random Delay 0 - 0.5 seconds between each colour change
import board
import time
from random import randint, uniform
import neopixel
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05)
while True:
    Rand = randint(0, 255), randint(0, 255), randint(0, 255)
    for Loop in range(10):
        np[Loop] = Rand
    np.show()
    time.sleep(uniform(0, .5))
