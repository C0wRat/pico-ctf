import hashlib

# Prompt the user to enter an MD5 hash to crack
hash_to_crack = open(input("Enter Hash File"), 'rb').read()

#opens the dictonary

with open("dictionary.txt", "r") as d:
    for combination in d:    # Iterate over each combination
        hash = hashlib.md5(combination.strip().encode()).digest()
        if hash == hash_to_crack:
            print("The password is:", combination)
            break
    else:
        print("Sorry, the password could not be cracked.")



# Big thanks to chat-gpt for this one :)
