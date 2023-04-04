import hashlib

# Generate all possible 4-digit combinations of 0-9 and a-z
charset = '0123456789abcdefghijklmnopqrstuvwxyz'
combinations = [a+b+c+d for a in charset for b in charset for c in charset for d in charset]

# Generate the corresponding hashes and store them in a dictionary
rainbow_table = {}
for combination in combinations:
    hash = hashlib.md5(combination.encode()).hexdigest()
    rainbow_table[hash] = combination

# Output the rainbow table to a file
with open("rainbow_table.txt", "wb") as f:
    for hash, combination in rainbow_table.items():
        f.write(hash.encode('utf-8') + ":".encode('utf-8') + combination.encode('utf-8') + "\n".encode('utf-8'))





# Big thanks to chat-gpt for this one :)
