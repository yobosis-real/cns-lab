# Simple Vigenere Cipher

def cipher(text, key, mode):
    result = ""
    key = key.lower()

    for i in range(len(text)):
        if text[i].isalpha():
            t = ord(text[i].lower()) - 97
            k = ord(key[i % len(key)]) - 97

            if mode == "e":
                x = (t + k) % 26
            else:
                x = (t - k) % 26

            result += chr(x + 65)

    return result


msg = "HELLO"
key = "KEY"

enc = cipher(msg, key, "e")
dec = cipher(enc, key, "d")

print("Encrypted:", enc)
print("Decrypted:", dec)
