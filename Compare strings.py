import vinTerminalFormatting as v

while True:
    str1 = input("1: ")
    str2 = input("2: ")
    if sorted(str1) == sorted(str2):
        v.printSpecial("Same", v.Red+v.Bright)
    else:
        v.printSpecial("NOT Same", v.Red+v.Bright)
    print("")
