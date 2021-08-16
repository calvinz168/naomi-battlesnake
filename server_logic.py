import random
from typing import List, Dict
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['w', 'a', 's', 'd']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        if k == 'w':
            return "up"
        elif k == "a":
            return "left"
        elif k == "s":
            return "down"
        elif k == "d":
            return "right"

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

