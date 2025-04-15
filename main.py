import time
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from blink1.blink1 import blink1

def color_equal(color1, color2):
    return all(abs(c1 - c2) < 10 for c1, c2 in zip(color1, color2))



previous_color = (0, 0, 0) #initial color of tray icon from Teams
with blink1() as b1:

    custom_press = False
    def on_press(key):
        global custom_press
        if key == Key.f1:
            custom_press = True
            b1.fade_to_color(100, 'red')
        elif key == Key.f2:
            custom_press = True
            b1.fade_to_color(100, 'orange')
        elif key == Key.f3:
            custom_press = True
            b1.fade_to_color(100, 'green')
        elif key == Key.f4:
            custom_press = False
            b1.off()


    # Collect events until released
    # with Listener(on_press=on_press) as listener:
    #     listener.join()

    try:
        while True:
            px = ImageGrab.grab().load()
            color = px[530, 1550] #color of tray icon from Teams

            if custom_press==False and color_equal(color, previous_color) == False:
                previous_color = color
                b1.play_pattern('5, #FF0000,0.2,0,#000000,0.2,0')
                time.sleep(2.0)
                b1.fade_to_rgb(100, color[0], color[1], color[2])
            time.sleep(5)
    except KeyboardInterrupt:
        b1.off()