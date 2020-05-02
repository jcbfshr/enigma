import secrets,string
from collections import OrderedDict

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

# convert character in alphabet to alphabet pos integer
def to_alphabet_pos(char):
    return list(string.ascii_uppercase).index(char.upper())

# convert character in alphabet to alphabet pos integer
def to_char(pos):
    return list(string.ascii_uppercase)[pos]

# move to rotor position
def cycle(list,pos):
    for i in range(pos):
        list.append(list[0])
        list.pop(0)
    return list

# rotor to create substition cipher
class Rotor:
    # rotor using alphabet set at position pos
    def __init__(self,offset=0):
        self.alphabet = []
        while len(self.alphabet) != 26:
            random = secrets.randbelow(26)
            if random not in self.alphabet:
                self.alphabet.append(random)
        self.offset = offset
        self.alphabet = cycle(self.alphabet,self.offset)
    
    # move the rotor by x position(s)
    def step(self,x=1):
        self.offset = (self.offset + x) % len(self.alphabet)
        self.alphabet = cycle(self.alphabet,self.offset)
    
    # substitute plaintext character with ciphertext character
    def substitute(self,char):
        self.step()
        return to_char(self.alphabet.index(to_alphabet_pos(char)))

class Reflector:
    # rotor using alphabet set at position pos
    def __init__(self,offset=0):
        self.alphabet = []
        while len(self.alphabet) != 26:
            random = secrets.randbelow(26)
            if random not in self.alphabet and len(self.alphabet) != random:
                self.alphabet.append(random)
        self.offset = offset
        self.alphabet = cycle(self.alphabet,self.offset)
    
    # substitute plaintext character with ciphertext character
    def substitute(self,char):
        return to_char(self.alphabet.index(to_alphabet_pos(char)))

rotors = [Rotor(int(input(f"Starting character for rotor {write_roman(i+1)}: "))) for i in range(3)]
rotors.append(Reflector())

plaintext = input("Plaintext: ").upper()
ciphertext = ""
for char in plaintext:
    cipherchar = char
    for i in range(2):
        for rotor in rotors:
            if i == 1 and rotors.index(rotor) == len(rotors)-1:
                break
            cipherchar = rotor.substitute(cipherchar)
    ciphertext += cipherchar
print(ciphertext)