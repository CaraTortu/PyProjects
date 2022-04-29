import pyautogui as pyg
import time as tm
from pynput.keyboard import Listener

def on_press(key):
    print(pyg.position(), key)

tm.sleep(3)

with Listener(on_press=on_press) as listener:
    listener.join()