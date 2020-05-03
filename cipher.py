import algo,secrets,store

# rotor to create substition cipher
class Rotor:
    def __init__(self,number,alphabet=-1,offset=-1,turnover=-1,alphabet_size=95,disc_type="rotor"):
        # -1 values signify randomise
        
        self.number = number

        if alphabet == -1:
            self.alphabet = []
            while len(self.alphabet) != alphabet_size:
                random = secrets.randbelow(alphabet_size)
                if random not in self.alphabet:
                    self.alphabet.append(random)
        else:
            self.alphabet = alphabet

        if offset == -1: 
            self.offset = secrets.randbelow(alphabet_size)
        else:
            self.offset = offset
        # apply offset to alphabet
        self.alphabet = algo.cycle(self.alphabet,self.offset)

        if turnover == -1:
            self.turnover = secrets.randbelow(alphabet_size)
        else:
            self.turnover = turnover
        
        self.steps = 0
        self.disc_type = disc_type
    
    # move the rotor by x position(s)
    def step(self,x=1):
        self.steps += x
        self.alphabet = algo.cycle(self.alphabet,x)
    
    # substitute plaintext character with ciphertext character
    def substitute(self,char,decrypt=False):
        # run char through opposite direction if decrypting
        if decrypt:
            return algo.to_char(self.alphabet[algo.to_alphabet_pos(char)])
        else:
            return algo.to_char(self.alphabet.index(algo.to_alphabet_pos(char)))

# spacer disc, randomly steps the adjacent rotor by 1-94 steps
class Spacer:
    def __init__(self,number,alphabet=-1,alphabet_size=95,disc_type="spacer"):
        self.number = number

        if alphabet == -1:
            self.alphabet = []
            for i in range(alphabet_size):
                random = secrets.randbelow(2)
                if random:
                    random = secrets.randbelow(alphabet_size-1)+1
                self.alphabet.append(random)
        else:
            self.alphabet = alphabet

        self.steps = 0
        self.disc_type = disc_type
    
    # move the rotor by x position(s)
    def step(self,x=1):
        self.steps += x
        self.alphabet = algo.cycle(self.alphabet,x)

# decyption module given plaintext and number of rotors to encrypt with
def encrypt(plaintext,no_rotors):
    # randomise rotors
    rotors = [Rotor(i+1,-1,secrets.randbelow(95),secrets.randbelow(95)) for i in range(no_rotors)]
    rotors.insert(0,Spacer(0))
    ciphertext = ""

    for char in plaintext:
        cipherchar = char

        for rotor in rotors:
            # if rotor is a spacer disc (controls random stepping of adjacent rotor)
            if rotor.number == 0:
                rotor.step()
                rotors[1].step(rotor.alphabet[0])
            else:
                # pass unsupported characters
                try:
                    cipherchar = rotor.substitute(cipherchar)
                except ValueError:
                    cipherchar = cipherchar

        ciphertext += cipherchar
        print(cipherchar,end="") # print characters as encrypted (stream)
    print()

    x = str(secrets.randbelow(1000))
    while len(x) != 3:
        x = "0" + x

    store.store(rotors,x)
    return x

# decyption module given ciphertext and rotors used to encrypt
def decrypt(ciphertext,rotors):
    plaintext = ""

    for char in ciphertext:
        # return rotors to position when encrypting original char
        for rotor in rotors:
            # if rotor is a spacer disc (controls random stepping of adjacent rotor)
            if rotor.type == "spacer":
                rotor.step()
                algo.cycle(rotors[1].alphabet,rotor.alphabet[0])

        plainchar = char

        # return encrypted char through rotors in opposite direction 
        for x in range(len(rotors)-1,0,-1):
            # pass unsupported characters
            try:
                plainchar = rotors[x].substitute(plainchar,True)
            except ValueError:
                plainchar = plainchar
        
        plaintext += plainchar
        print(plainchar,end="") # print characters as encrypted (stream)
    print()