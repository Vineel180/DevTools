import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, Compare strings")

while True:
    str1 = v.inputSpecial("1: ", "", v.Blue)
    str2 = v.inputSpecial("2: ", "", v.Blue)
    if str1 == str2:
        v.printSpecial("[ Same ]", v.Green+v.Bright)
    else:
        v.printSpecial("[ NOT Same ]", v.Green+v.Bright)
    print("")
