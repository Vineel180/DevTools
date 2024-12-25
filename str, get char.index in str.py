import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, get char.index in str")

while True:
    userInput = input("String: ")
    start = -1
    end = 0
    for i in userInput:
        start += 1
        end -= 1
        v.printSpecial(i, v.Red+v.Bold, "")
        print(" | ", end="")
        v.printSpecial(start, v.Green+v.Bold, "")
        print(" | ", end="")
        v.printSpecial(end, v.Blue+v.Bold)
    print()
