# Convert letter ↔ number
def to_num(c):
    return ord(c) - ord('a')

def to_char(n):
    return chr(n + ord('a'))


# Generate repeated key
def make_key(text, key):
    key = key.lower()
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            result += key[j % len(key)]
            j += 1
        else:
            result += ch

    return result


# Encrypt
def encrypt(text, key):
    text = text.lower()
    key = make_key(text, key)

    result = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (to_num(text[i]) + to_num(key[i])) % 26
            result += to_char(x)
        else:
            result += text[i]

    return result.upper()


# Decrypt
def decrypt(text, key):
    text = text.lower()
    key = make_key(text, key)

    result = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (to_num(text[i]) - to_num(key[i])) % 26
            result += to_char(x)
        else:
            result += text[i]

    return result


# Example
msg = "HELLO WORLD"
key = "KEY"

enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
