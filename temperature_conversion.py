
def convert_temperature(temp):
    degree = int(temp[:-1])
    i_conv = temp[-1]

    if i_conv.upper() == "C":
        convert = int(round((9 * degree) / 5 + 32))
        o_conv = "Fahrenheit"
    elif i_conv.upper() == "F":
        convert = int(round((degree - 32) * 5 / 9))
        o_conv = "Celsius"
    else:
        print("Input proper convention.")
        quit()
    print("The temperature in", o_conv, "is", convert, "degrees.")


temperature = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
convert_temperature(temperature)
