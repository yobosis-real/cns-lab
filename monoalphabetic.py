import string

key = "qwertyuiopasdfghjklzxcvbnm"

a = string.ascii_lowercase
enc_map = str.maketrans(a, key)
dec_map = str.maketrans(key, a)

msg = "Hello World"

enc = msg.lower().translate(enc_map)
dec = enc.translate(dec_map)

print("Encrypted:", enc)
print("Decrypted:", dec)
