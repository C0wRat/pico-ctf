from itertools import product

flag_enc = open('secret.txt', 'rb').read()

print
secret = []
key = []
possible_chars = ["0","1","2","3","4","5","6","7","8","9"]

# The decryption algorithm
def str_xor(secret, key):
    out = []
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    for (secret_c,new_key_c) in zip(secret,new_key):
        out.append(chr(ord(secret_c) ^ ord(new_key_c)))
    with open('decrypted.txt', 'a') as f:
        f.write(''.join(out))
        f.write("\n")

    return ''.join(out)




# The Brute force algo, this works due to us knowing the first 8 characters of the encrypted data
def find_known_letter(letter: chr, index: int, flag_enc: str, secret: list, key: list):
    val = 0
    for val in possible_chars:
        guess = chr(ord(str(val)) ^ ord(chr(flag_enc[index])))
        if guess == letter:
            secret.append(guess)
            key.append(str(val))
            return True



def brute_force():
    print("brute selected")
    pword_len = input("Enter Length of password:")
    print("generating acii table...")
    print("generating possible keys..")
    combinations = list(product(possible_chars, repeat=int(pword_len)))
    print("Trying Keys...")
    for key in combinations:
        str_xor(flag_enc.decode(), ''.join(key))
    print("Done...")


    return True

# used because we know the first 8 characters of the encrypted data, can easily be changed if we know specific elements of the secret.
def pico_brute_force():
    find_known_letter('p', 0, flag_enc, secret, key) # used to find the letter 'p'
    find_known_letter('i', 1, flag_enc, secret, key) # used to find the letter 'i'
    find_known_letter('c', 2, flag_enc, secret, key) # used to find the letter 'c'
    find_known_letter('o', 3, flag_enc, secret, key) # used to find the letter 'o'
    find_known_letter('C', 4, flag_enc, secret, key) # used to find the letter 'C'
    find_known_letter('T', 5, flag_enc, secret, key) # used to find the letter 'T'
    find_known_letter('F', 6, flag_enc, secret, key) # used to find the letter 'F'
    find_known_letter('{', 7, flag_enc, secret, key) # used to find the letter '{'

    print ("found: ", "".join(secret))
    print ("key: ", "".join(key))


option = input("Options\n------------\npico\nbrute\ndecrypt\n: ")
if option == "pico":
    pico_brute_force()
elif option == "brute":
    brute_force()
elif option == "decrypt":
    key = input("Enter Key: ")
    print(str_xor(flag_enc.decode(), key))