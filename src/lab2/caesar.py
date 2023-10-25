""" Caesar cipher """


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha():
            if symbol.islower():
                ciphertext += chr((ord(symbol) - 97 + shift) % 26 + 97)
            else:
                ciphertext += chr((ord(symbol) - 65 + shift) % 26 + 65)
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for symbol in ciphertext:
        if symbol.isalpha():
            if symbol.islower():
                plaintext += chr((ord(symbol) - 97 - shift) % 26 + 97)
            else:
                plaintext += chr((ord(symbol) - 65 - shift) % 26 + 65)
        else:
            plaintext += symbol
    return plaintext
