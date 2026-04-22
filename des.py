from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'  # 8 bytes key

msg = input("Enter message: ").encode()

# Encrypt
cipher = DES.new(key, DES.MODE_ECB)
enc = cipher.encrypt(pad(msg, 8))
print("Encrypted:", enc)

# Decrypt
cipher = DES.new(key, DES.MODE_ECB)
dec = unpad(cipher.decrypt(enc), 8)
print("Decrypted:", dec.decode())
