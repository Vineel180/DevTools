import os
import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle()

def getUserPath():
    return type((os.environ.get("PATH")))#.split(";").sort()
def getSystemPath():
    return (os.environ.get("SystemRoot"))#.split(";").sort()

while True:
    userInput = v.inputSpecial("0: Both. 1: User path. 2: System path. | ")
    if userInput == "0":
        print(getUserPath())
        print(getSystemPath())
