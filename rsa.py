import random
from math import gcd

# Check prime
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

# Get random prime
def get_prime():
    while True:
        n = random.randint(50, 100)
        if is_prime(n):
            return n


# Step 1: generate p, q
p = get_prime()
q = get_prime()
while p == q:
    q = get_prime()

# Step 2: n and phi
n = p * q
phi = (p-1)*(q-1)

# Step 3: choose e
e = random.randint(2, phi-1)
while gcd(e, phi) != 1:
    e = random.randint(2, phi-1)

# Step 4: find d
d = 1
while (e * d) % phi != 1:
    d += 1

print("Public key:", (e, n))
print("Private key:", (d, n))


# Encrypt
msg = int(input("Enter number: "))
enc = pow(msg, e, n)
print("Encrypted:", enc)

# Decrypt
dec = pow(enc, d, n)
print("Decrypted:", dec)
