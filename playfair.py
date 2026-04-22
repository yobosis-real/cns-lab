alphabet = "abcdefghiklmnopqrstuvwxyz"  # no 'j'

# Create matrix
def create_matrix(key):
    key = key.lower().replace("j", "i")
    matrix = ""

    for ch in key + alphabet:
        if ch not in matrix:
            matrix += ch

    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]


# Find position
def find(mat, ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j


# Prepare text into pairs
def prepare(text):
    text = text.lower().replace("j", "i")
    text = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "x"

        if a == b:
            result += a + "x"
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += "x"

    return result


# Encrypt
def encrypt(text, key):
    mat = create_matrix(key)
    text = prepare(text)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find(mat, a)
        r2, c2 = find(mat, b)

        if r1 == r2:  # same row
            result += mat[r1][(c1+1)%5] + mat[r2][(c2+1)%5]

        elif c1 == c2:  # same column
            result += mat[(r1+1)%5][c1] + mat[(r2+1)%5][c2]

        else:  # rectangle
            result += mat[r1][c2] + mat[r2][c1]

    return result.upper()


# Decrypt
def decrypt(text, key):
    mat = create_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i].lower(), text[i+1].lower()
        r1, c1 = find(mat, a)
        r2, c2 = find(mat, b)

        if r1 == r2:
            result += mat[r1][(c1-1)%5] + mat[r2][(c2-1)%5]

        elif c1 == c2:
            result += mat[(r1-1)%5][c1] + mat[(r2-1)%5][c2]

        else:
            result += mat[r1][c2] + mat[r2][c1]

    return result


# Example
key = "monarchy"
msg = "instruments"

enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
