# Convert letter ↔ number
def to_num(c):
    return ord(c) - ord('a')

def to_char(n):
    return chr(n + ord('a'))


# Encrypt
def encrypt(text, key):
    text = text.lower().replace(" ", "")
    
    # make even length
    if len(text) % 2 != 0:
        text += 'x'

    result = ""

    for i in range(0, len(text), 2):
        a = to_num(text[i])
        b = to_num(text[i+1])

        # matrix multiplication
        x = (key[0][0]*a + key[0][1]*b) % 26
        y = (key[1][0]*a + key[1][1]*b) % 26

        result += to_char(x) + to_char(y)

    return result.upper()


# Decrypt (using inverse matrix)
def decrypt(text, key):
    # determinant
    det = key[0][0]*key[1][1] - key[0][1]*key[1][0]
    det = det % 26

    # find inverse of determinant (brute force)
    for i in range(26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    # inverse matrix
    inv = [
        [ key[1][1]*inv_det % 26, -key[0][1]*inv_det % 26],
        [-key[1][0]*inv_det % 26,  key[0][0]*inv_det % 26]
    ]

    result = ""

    for i in range(0, len(text), 2):
        a = to_num(text[i].lower())
        b = to_num(text[i+1].lower())

        x = (inv[0][0]*a + inv[0][1]*b) % 26
        y = (inv[1][0]*a + inv[1][1]*b) % 26

        result += to_char(x) + to_char(y)

    return result


# Example
key = [[3, 3],
       [2, 5]]

msg = "help"

enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
