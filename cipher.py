import algo,secrets

# rotor to create substition cipher
class Rotor:
    # rotor using alphabet set at position pos
    def __init__(self,number,alphabet=-1,offset=-1,turnover=-1,alphabet_size=95):
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
        self.alphabet = algo.cycle(self.alphabet,self.offset)
        if turnover == -1:
            self.turnover = secrets.randbelow(alphabet_size)
        else:
            self.turnover = turnover
    
    # move the rotor by x position(s)
    def step(self,x=1):
        self.alphabet = algo.cycle(self.alphabet,x)
    
    # substitute plaintext character with ciphertext character
    def substitute(self,char,decrypt=False):
        if decrypt:
            return algo.to_char(self.alphabet[algo.to_alphabet_pos(char)])
        else:
            return algo.to_char(self.alphabet.index(algo.to_alphabet_pos(char)))