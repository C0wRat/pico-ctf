import hashlib

# Prompt the user to enter an MD5 hash to crack
hash_to_crack = open(input("Enter Hash File"), 'rb').read()

# Generate all possible 4-digit combinations of 0-9 and a-z
charset = '0123456789abcdefghijklmnopqrstuvwxyz'
combinations = [a+b+c+d for a in charset for b in charset for c in charset for d in charset]

# Iterate over each combination, hash it, and compare to the target hash
for combination in combinations:
    hash = hashlib.md5(combination.encode()).digest()
    #print(combination,":",hash,"=",hash_to_crack)
    if hash == hash_to_crack:
        print("The password is:", combination)
        break
else:
    print("Sorry, the password could not be cracked.")


# Big thanks to chat-gpt for this one :)
