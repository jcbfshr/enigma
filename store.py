import json,algo

def store(rotors,filename,alphabet_size=95):
    file = open(str(filename)+".rotors","w")
    x = {}
    for rotor in rotors:
        x[rotors.index(rotor)] = [algo.cycle(rotor.alphabet,alphabet_size-rotor.offset),rotor.offset,rotor.turnover]
    file.write(json.dumps(x))
    file.close()

def load(filename):
    file = open(str(filename)+".rotors","r")
    y = json.loads(file.read())
    file.close()
    return y