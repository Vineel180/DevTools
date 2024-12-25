import vinTerminalFormatting as v
from pyautogui import position
from time import sleep

print(v.Green + v.Bold)
while True:
    x, y = position()
    print(f"  [X: {x}]  [Y: {y}]          ", end="\r")
    sleep(0.04)
