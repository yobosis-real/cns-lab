# Simple Diffie Hellman

p = 23
g = 5

a = 6   # Private key A
b = 15  # Private key B

# Public keys
A = (g ** a) % p
B = (g ** b) % p

print("Public Key A:", A)
print("Public Key B:", B)

# Secret key
key1 = (B ** a) % p
key2 = (A ** b) % p

print("Key A:", key1)
print("Key B:", key2)

if key1 == key2:
    print("Key Exchange Successful")
