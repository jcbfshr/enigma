import cipher,store
from progress.bar import ShadyBar

mode = str(input("Encrypt (y/n): "))[0].lower()

if mode == "y":
    no_rotors = int(input("Number of rotors: "))
    print(f"Use key {cipher.encrypt(input('Plaintext: '),no_rotors)}.rotors to encrypt")
elif mode == "n":
    rotor_settings = store.load(str(input("Rotor settings reference (35 chars): "))[:34])
    rotors = []

    print("Setting rotors . . .")

    for i in range(len(rotor_settings)):
        rotor = rotor_settings[str(i)]
        if rotor[0] == "spacer":
            rotors.append(cipher.Spacer(i,rotor[1]))
        else:
            rotors.append(cipher.Rotor(i,rotor[1],rotor[2],rotor[3]))
    cipher.decrypt(input("Ciphertext: "),rotors)
else:
    print("Output not recognised, please type only \'y\' or \'n\'")