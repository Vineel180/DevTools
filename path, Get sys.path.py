import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("path, Get sys.path")

while True:
    from sys import path as sysPath

    for i in sysPath.sort():
        print(i)
    print()

    userInput = v.inputSpecial("Enter folder path: ", v.Blue, v.Blue+v.Bold)
    if userInput in sysPath:
        v.printSpecial("[ YES ]", v.Green+v.Bold)
    else:
        v.printSpecial("[ NO ]", v.Green+v.Bold)
    print()

    v.inputSpecial("Press Enter to continue. ", v.Dim)
    print()
