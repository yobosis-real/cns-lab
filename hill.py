# Simple Hill Cipher

key = [[3, 3], [2, 5]]

def hill(text):
    text = text.lower()
    result = ""

    for i in range(0, len(text), 2):
        a = ord(text[i]) - 97
        b = ord(text[i+1]) - 97

        x = (3*a + 3*b) % 26
        y = (2*a + 5*b) % 26

        result += chr(x + 65) + chr(y + 65)

    return result

msg = "help"

enc = hill(msg)

print("Encrypted:", enc)
