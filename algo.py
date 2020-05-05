import string
from collections import OrderedDict

# create alphabetical arrary given upper and lower bound
class Alphabet:
    def __init__(self,lower=" ",upper="~"):
        self.lower = ord(lower)
        self.upper = ord(upper)+1
        self.alphabet = [chr(i) for i in range(self.lower,self.upper)]

print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))

# move first item in list to back pos times
def cycle(list,pos):
    for each in list:
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

# print list with commas and 'and' before last item
def format_english_list(x):
    string = ""
    for i in range(len(x)):
        string += x[i]
        if i == (len(x)-2):
            string += " or "
        elif i != (len(x)-1):
            string += ", "
    return string

# only accept responses found in valid list
def validate_input(string,valid=["y","n","exit"]):
    while True:
        x = input(string).lower()
        if x in valid:
            break
        else:
            print(f"Input not recognised, please input only {format_english_list(valid)}")
    return x
