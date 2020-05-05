import json,algo,cipher,tqdm

# load contents of user file (name)
def contents(string="File: "):
    while True:
        # if file exists
        try:
            ref = str(input(string))
            file = open(ref,"r")
            contents = file.read()
            file.close()
            break
        except FileNotFoundError:
            print("File not found")
    return [contents,ref]

# store rotor configuration in file
def store(rotors,filename,alphabet_size):
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
def load():
    file = open(contents("Rotor settings reference (35 chars): ")[0],"r")
    rotor_settings = json.loads(file.read())
    file.close()

    rotors = []

    for i in tqdm.trange(len(rotor_settings)):
        rotor = rotor_settings[str(i)]
        if rotor[0] == "spacer":
            rotors.append(cipher.Spacer(i,rotor[1]))
        else:
            rotors.append(cipher.Rotor(i,rotor[1],rotor[2],rotor[3]))
    return rotors