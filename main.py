import time
from PIL import ImageGrab
from blink1.blink1 import blink1

def color_equal(color1, color2):
    return all(abs(c1 - c2) < 10 for c1, c2 in zip(color1, color2))

previous_color = (0, 0, 0) #initial color of tray icon from Teams
with blink1() as b1:
    while True:
        px = ImageGrab.grab().load()
        color = px[2183, 1568] #color of tray icon from Teams

        if color_equal(color, previous_color):
            b1.play_pattern('5, #FF0000,0.2,0,#000000,0.2,0')
            time.sleep(2.0)
        b1.fade_to_rgb(100, color[0], color[1], color[2])
        time.sleep(5)