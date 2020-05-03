import cipher,algo,secrets,store,time

start = time.time()

mode = str(input("Encrypt (y/n): "))[0].lower()

if mode == "y":
    no_rotors = int(input("Number of rotors: "))
    rotors = [cipher.Rotor(i,-1,secrets.randbelow(95),secrets.randbelow(95)) for i in range(no_rotors)]
    plaintext = input("Plaintext: ")
    ciphertext = ""

    for char in plaintext:
        cipherchar = char
        for rotor in rotors:

            try:
                cipherchar = rotor.substitute(cipherchar)
            except ValueError:
                if cipherchar == " ":
                    cipherchar = rotor.substitute("X")
                cipherchar = cipherchar
        ciphertext += cipherchar
        print(cipherchar,end="")
    print()

    x = str(secrets.randbelow(1000))
    while len(x) != 3:
        x = "0" + x

    store.store(rotors,"000")

    # # print(algo.format(ciphertext,4))
    # print(ciphertext)
elif mode == "n":
    rotor_settings = store.load(str(input("Rotor settings reference (3 digits): "))[:3])
    rotors = []

    for i in range(len(rotor_settings)):
        rotor = rotor_settings[str(i)]
        # if i == 0:
        #     rotors.append(cipher.Spacer(i,rotor[0]))
        # else:
        rotors.append(cipher.Rotor(i,rotor[0],rotor[1],rotor[2]))
    
    ciphertext = input("Ciphertext: ")
    plaintext = ""

    for char in ciphertext:
        plainchar = char
        for x in range(len(rotors)-1,-1,-1):

            try:
                plainchar = rotors[x].substitute(plainchar,True)
            except ValueError:
                plainchar = plainchar
        plaintext += plainchar
        print(plainchar,end="")
    print()
else:
    print("Output not recognised, please type only \'y\' or \'n\'")

# execution time
print(str(round((time.time() - start)*100))+"ms")