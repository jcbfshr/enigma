import cipher,store,tqdm,algo,random,time

print("""
    Jacob Fisher, MMXX

    - never use the same key twice for encryption, a random key is generated every time for encryption
    - type exit to close the program

""")

mode = algo.validate_input("Encrypt (y/n): ")

# ENCRYPTION
if mode == "y":
    while True:
        # only accept integers
        try:
            no_rotors = abs(int(input("Number of rotors: ")))
            break
        except ValueError:
            print("Please only enter a natural number")
    # randomise rotors
    rotors = cipher.create_rotors(no_rotors)

    using_file = algo.validate_input("Encrypt a file (y/n): ")
    if using_file == "y":
        unencrypted_file = store.contents()

        for i in tqdm.trange(len(unencrypted_file[0])):
            ciphertext += cipher.decrypt(unencrypted_file[0][i],rotors)

        # overwrite file with encrypted contents
        file = open(unencrypted_file[1],"w")
        file.write(ciphertext)
        file.close()

    elif using_file == "n":
        plaintext = str(input("Plaintext: "))
        ciphertext = ""

        bar = tqdm.trange(len(plaintext),desc='ML', leave=True)

        for i in bar:
            ciphertext += cipher.encrypt(plaintext[i],rotors)
            bar.set_description(ciphertext)
            bar.refresh()
    # Create hex key name and store as file
    x = hex(random.getrandbits(128))
    store.store(rotors,str(x),cipher.get_alphabet_size())
    print(f"Use key {x}.rotors to decrypt")

# DECRYPTION
elif mode == "n":
    rotors = store.load()
    
    using_file = algo.validate_input("Decrypt a file (y/n): ")
    if using_file == "y":
        encrypted_file = store.contents()
        plaintext = ""

        for i in tqdm.trange(len(encrypted_file[0])):
            plaintext += cipher.decrypt(encrypted_file[0][i],rotors)

        # overwrite file with decrypted contents
        file = open(encrypted_file[1],"w")
        file.write(plaintext)
        file.close()
    
    elif using_file == "n":
        ciphertext = str(input("Ciphertext: "))
        plaintext = ""

        for i in tqdm.trange(len(plaintext)):
            plaintext += cipher.decrypt(ciphertext[i],rotors)