import cipher,store,progressbar,algo

widgets=[
            ' [', progressbar.Timer(), '] ',
            progressbar.Bar(marker="█"),
            ' (', progressbar.ETA(), ') ',
        ]

print("""
    Jacob Fisher, MMXX

    - never use the same key twice for encryption, a random key is generated every time for encryption
    - use more than 5,000 rotors
    - vary the number of rotors used
    - type exit to close the program

""")

mode = algo.validate_input("Encrypt (y/n): ")

if mode == "y":
    no_rotors = int(input("Number of rotors: "))
    using_file = algo.validate_input("Encrypt file (y/n): ")
    if using_file == "y":
        while True:
            try:
                # if file exists
                ref = str(input("File: "))
                file = open(ref,"r")
                contents = file.read()
                file.close()
                break
            except FileNotFoundError:
                print("File not found")

        cipher_return = cipher.encrypt(contents,no_rotors,True)
        print(f"Use key {cipher_return[1]}.rotors to decrypt")
        file = open(ref,"w")
        file.write(cipher_return[0])
        file.close()
    
    elif using_file == "n":
        print(f"Use key {cipher.encrypt(input('Plaintext: '),no_rotors)}.rotors to decrypt")
elif mode == "n":
    rotor_settings = store.load(str(input("Rotor settings reference (35 chars): "))[:34])
    rotors = []

    for i in progressbar.progressbar(range(len(rotor_settings)),widgets=widgets):
        rotor = rotor_settings[str(i)]
        if rotor[0] == "spacer":
            rotors.append(cipher.Spacer(i,rotor[1]))
        else:
            rotors.append(cipher.Rotor(i,rotor[1],rotor[2],rotor[3]))
    
    using_file = algo.validate_input("Decrypt file (y/n): ")
    if using_file == "y":
        while True:
            try:
                # if file exists
                ref = str(input("File: "))
                file = open(ref,"r")
                contents = file.read()
                file.close()
                break
            except FileNotFoundError:
                print("File not found")

        file = open(ref,"w")
        file.write(cipher.decrypt(contents,rotors,True))
        file.close()
    
    elif using_file == "n":
        cipher.decrypt(input("Ciphertext: "),rotors)