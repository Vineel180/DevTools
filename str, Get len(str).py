import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, Get len(str)")

while True:
    userInput = v.inputSpecial("String: ", "", v.Blue)
    v.printSpecial(f"Length: {len(userInput)}", v.Green+v.Bold)
    print()
