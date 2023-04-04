key = "8713"
secret = "幈屒捻䡷̍嬄䕧崀ٟ呟٧œ卞ଇ䨋"

new_key = key
i = 0
while len(new_key) < len(secret):
    new_key = new_key + key[i]
    i = (i + 1) % len(key)
    

key = "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
