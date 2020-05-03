import string
from collections import OrderedDict

alphabet = [chr(i) for i in range(32,127)]

# convert character in alphabet to alphabet pos integer
def to_alphabet_pos(char):
    return alphabet.index(char)

# convert character in alphabet to alphabet pos integer
def to_char(pos):
    return alphabet[pos]

# move to rotor position
def cycle(list,pos):
    for i in range(pos):
        list.append(list[0])
        list.pop(0)
    return list

# add space between every x characters in string
def format(string,x):
    list = [string[i:i+x] for i in range(0, len(string), x)]
    string = ""
    for i in range(len(list)):
        string += list[i]
        if (i+1) % x == 0:
            string += "\n"
        else:
            string += " "
    return string

# convert integer to roman numeral
def write_roman(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])