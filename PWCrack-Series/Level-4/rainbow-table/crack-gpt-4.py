import hashlib


# Prompt the user to enter an MD5 hash to look up
hash_to_lookup = open(input("Enter Hash File"), 'rb').read()

# Load the rainbow table from file
rainbow_table = {}
with open("rainbow_table.txt", "r") as f:
    for line in f:
        hash, combination = line.strip().split(":")
        rainbow_table[bytes.fromhex(hash)] = combination


# Look up the corresponding combination in the rainbow table
if hash_to_lookup in rainbow_table:
    print("The combination for the hash", hash_to_lookup, "is", rainbow_table[hash_to_lookup])
else:
    print("Sorry, the hash", hash_to_lookup, "was not found in the rainbow table.")



#big thanks to chat-gpt for this one :)
