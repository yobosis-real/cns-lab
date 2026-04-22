from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate keys
key = RSA.generate(2048)

msg = input("Enter message: ").encode()

# Hash
h = SHA256.new(msg)

# Sign
sig = pkcs1_15.new(key).sign(h)
print("Signature:", sig)

# Verify
try:
    pkcs1_15.new(key.publickey()).verify(h, sig)
    print("Valid signature")
except:
    print("Invalid signature")
