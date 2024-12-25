from vinBase import *
import vinTerminalFormatting as v
import os
import winreg
v.setAndPrintSpecialTerminalTitle("path, Get user and system.path")

def getUserPaths():
    return sorted((os.environ.get("PATH", "")).split(";"))
def getSystemPaths():
    registryKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
    systemPaths, garbageVar = winreg.QueryValueEx(registryKey, "Path")
    winreg.CloseKey(registryKey)
    return sorted(systemPaths.split(";"))

if __name__ == "__main__":
    while True:
        userPaths = getUserPaths()
        systemPaths_base = getSystemPaths()

        systemPaths = []
        for i in systemPaths_base:
            if i:
                systemPaths.append(i)

        uniqueUserPaths = []
        for i in userPaths:
            if i not in systemPaths:
                uniqueUserPaths.append(i)
        userPaths = uniqueUserPaths
        ###
        v.printSpecial("System path variables: ", v.Yellow)
        thisLen = len(systemPaths)
        for i in range(thisLen):
            print(f"{v.Yellow}{v.getSameLengthNumber_instanceIterator(i+1, thisLen+1)}: {v.Reset}{systemPaths[i]}")
        v.printSpecial("User path variables: ", v.Yellow)
        thisLen = len(userPaths)
        for i in range(thisLen):
            print(f"{v.Yellow}{v.getSameLengthNumber_instanceIterator(i+1, thisLen+1)}: {v.Reset}{userPaths[i]}")
        p()

        userInput = (v.inputSpecial("Enter path: ", v.Blue, v.Blue+v.Bright)).strip()
        if userInput in systemPaths:
            v.printSpecial("[ Path in SYSTEM Paths. ]", v.Green+v.Bold)
        elif userInput in uniqueUserPaths:
            v.printSpecial("[ Path in USER Paths ].", v.Green+v.Bold)
        else:
            v.printSpecial("[ Path NOT found. ]", v.Green+v.Bold)
        p()

        v.inputSpecial("Press Enter to continue. ", v.Dim)
        p()
