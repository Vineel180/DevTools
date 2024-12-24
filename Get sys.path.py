import vinTerminalFormatting as v
from sys import path as sysPath

while True:
    for i in sysPath:
        print(i)
    print()

    userInput = v.inputSpecial("Enter folder path: ", v.Blue, v.Green+v.Bold)
    if userInput in sysPath:
        v.printSpecial("YES", v.Green+v.Bold)
    else:
        v.printSpecial("NO", v.Green+v.Bold)
    print()
