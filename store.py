import json,algo

# store rotor configuration in file
def store(rotors,filename,alphabet_size=95):
    file = open(str(filename)+".rotors","w")
    x = {}

    for rotor in rotors:
        if rotor.disc_type == "spacer":
            x[rotors.index(rotor)] = [rotor.disc_type,algo.cycle(rotor.alphabet,(alphabet_size-rotor.steps)%alphabet_size)]
        else:
            x[rotors.index(rotor)] = [rotor.disc_type,algo.cycle(algo.cycle(rotor.alphabet,(alphabet_size-rotor.steps)%alphabet_size),alphabet_size-rotor.offset),rotor.offset,rotor.turnover]
    
    file.write(json.dumps(x))
    file.close()

# load rotor configurations from file
def load(filename):
    file = open(str(filename)+".rotors","r")

    y = json.loads(file.read())
    file.close()
    return y