import string

# Create mapping
def create_mapping(key):
    return dict(zip(string.ascii_lowercase, key.lower()))

# Encrypt
def mono_encrypt(text, key):
    mapping = create_mapping(key)
    result = ""

    for ch in text:
        if ch.isalpha():
            new = mapping[ch.lower()]
            result += new.upper() if ch.isupper() else new
        else:
            result += ch

    return result

# Decrypt
def mono_decrypt(text, key):
    mapping = create_mapping(key)
    reverse = {v: k for k, v in mapping.items()}
    result = ""

    for ch in text:
        if ch.isalpha():
            new = reverse[ch.lower()]
            result += new.upper() if ch.isupper() else new
        else:
            result += ch

    return result


# Example
key = "qwertyuiopasdfghjklzxcvbnm"
msg = "Hello World"

enc = mono_encrypt(msg, key)
dec = mono_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
