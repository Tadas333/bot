
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Controller as keyController
import time

mouse = mouseController()
keyboard = keyController()


#time.sleep(3)


##mouse.position = (1920, 1080)


print('The current pointer position is {0}'.format(
    mouse.position))