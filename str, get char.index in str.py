import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, get char.index in str")

while True:
    userInput = input("String: ")
    lenOfUserInput = len(userInput)
    start = -1
    end = 0
    for i in userInput:
        start += 1
        end -= 1
        v.printSpecial(i, v.Red+v.Bold, "")
        print(" | ", end="")
        v.printSpecial(v.getSameLengthNumber_instanceIterator(start, lenOfUserInput, " ", False), v.Green+v.Bold, "")
        print(" | ", end="")
        v.printSpecial(v.getSameLengthNumber_instanceIterator(end, lenOfUserInput, " ", False), v.Blue+v.Bold)
    print()
