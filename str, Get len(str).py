import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, Get len(str)")

while True:
    userInput = input("String: ")
    v.printSpecial(f"Length: {len(userInput)}", v.Green+v.Bold)
    print()
