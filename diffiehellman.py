p = int(input("Enter prime p: "))
g = int(input("Enter primitive root g: "))

# Private keys
a = int(input("Private key of A: "))
b = int(input("Private key of B: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Public A:", A)
print("Public B:", B)

# Shared secret
key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Key (A):", key1)
print("Key (B):", key2)

print("Success!" if key1 == key2 else "Failed!")
