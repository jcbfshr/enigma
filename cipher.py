import algo,secrets,store,random,progressbar

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
    rotors = []

    widgets=[
        ' [', progressbar.Timer(), '] ',
        progressbar.Bar(marker="█"),
        ' (', progressbar.ETA(), ') ',
    ]

    for i in progressbar.progressbar(range(no_rotors),widgets=widgets):
        if i % 10 == 0:
            rotors.append(Spacer(i))
        else:
            rotors.append(Rotor(i,-1,secrets.randbelow(95),secrets.randbelow(95)))
    ciphertext = ""

    for char in plaintext:
        cipherchar = char

        for rotor in rotors:
            # if rotor is a spacer disc (controls random stepping of adjacent rotor)
            if rotor.disc_type == "spacer":
                rotor.step()
                rotors[rotors.index(rotor)+1].step(rotor.alphabet[0])
            else:
                if rotor.alphabet[0] == rotor.turnover:
                    rotors[rotors.index(rotor)+1].step()
                # pass unsupported characters
                try:
                    cipherchar = rotor.substitute(cipherchar)
                except ValueError:
                    cipherchar = cipherchar

        ciphertext += cipherchar
        print(cipherchar,end="") # print characters as encrypted (stream)
    print()

    x = hex(random.getrandbits(128))

    store.store(rotors,x)
    return x

# decyption module given ciphertext and rotors used to encrypt
def decrypt(ciphertext,rotors):
    plaintext = ""

    for char in ciphertext:
        # return rotors to position when encrypting original char
        for rotor in rotors:
            # if rotor is a spacer disc (controls random stepping of adjacent rotor)
            if rotor.disc_type == "spacer":
                rotor.step()
                rotors[rotors.index(rotor)+1].step(rotor.alphabet[0])
            elif rotor.alphabet[0] == rotor.turnover:
                rotors[rotors.index(rotor)+1].step()
        plainchar = char

        # return encrypted char through rotors in opposite direction 
        for x in range(len(rotors)-1,-1,-1):
            if rotors[x].disc_type != "spacer":
                # pass unsupported characters
                try:
                    plainchar = rotors[x].substitute(plainchar,True)
                except ValueError:
                    plainchar = plainchar
        
        plaintext += plainchar
        print(plainchar,end="") # print characters as encrypted (stream)
    print()