import vinTerminalFormatting as v
v.setAndPrintSpecialTerminalTitle("str, Compare sorted strings")

while True:
    str1 = v.inputSpecial("1: ", "", v.Blue)
    str2 = v.inputSpecial("2: ", "", v.Blue)
    if sorted(str1) == sorted(str2):
        v.printSpecial("[ Same ]", v.Green+v.Bright)
    else:
        v.printSpecial("[ NOT Same ]", v.Green+v.Bright)
    print("")
