def caesar(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch

    return result


msg = "Hello, World!"

enc = caesar(msg, 3)
dec = caesar(enc, -3)

print("Original :", msg)
print("Encrypted:", enc)
print("Decrypted:", dec)
