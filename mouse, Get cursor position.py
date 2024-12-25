import vinTerminalFormatting as v
from vinDateTime import getDateTimeWeekday
from pyautogui import position
from time import sleep
from pynput.keyboard import Key, Listener
import threading

outputLock = threading.Lock()
sharedSignal_forEnterKey = threading.Event()

def ifEnterKeyIsPressed_instance(key):
    if key == Key.enter:
        with outputLock:
            print(f"{v.Red}{getDateTimeWeekday()[8:10]}:{getDateTimeWeekday()[10:12]}:{getDateTimeWeekday()[12:14]} | {v.Reset}", end="")
        sharedSignal_forEnterKey.set()
        return True

def ifEnterKeyIsPressed():
    with Listener(on_press=ifEnterKeyIsPressed_instance) as listener:
        listener.join()

def getMousePosition():
    while True:
        x, y = position()
        with outputLock:
            if sharedSignal_forEnterKey.is_set():
                print(f"{v.Blue}[X: {x}]  [Y: {y}]                    {v.Reset}")
                sharedSignal_forEnterKey.clear()
            else:
                print(f"{v.Green}{v.Bold}  [X: {x}]  [Y: {y}]                    {v.Reset}", end="\r")
        sleep(0.04)

if __name__ == "__main__":
    mode = input("0: Std. Any: Print when ENTER. | ")
    v.clearScreen_And_sendCursorToHome()
    if mode == "0":
        v.setTerminalTitle("Single: mouse, Get cursor position")
        getMousePosition()
    else:
        v.setTerminalTitle("Dual: mouse, Get cursor position")
        thread_getMousePosition = threading.Thread(target=getMousePosition, daemon=True)
        thread_ifEnterKeyIsPressed = threading.Thread(target=ifEnterKeyIsPressed, daemon=True)
        thread_getMousePosition.start()
        thread_ifEnterKeyIsPressed.start()
        thread_getMousePosition.join()
        thread_ifEnterKeyIsPressed.join()
