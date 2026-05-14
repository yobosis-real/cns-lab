# Simple RSA with e Calculation

p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if phi % e != 0:
        break
    e += 1

d = 1
while (e * d) % phi != 1:
    d += 1

print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)

msg = int(input("Enter Number: "))

# Encryption
enc = (msg ** e) % n
print("Encrypted:", enc)

# Decryption
dec = (enc ** d) % n
print("Decrypted:", dec)
