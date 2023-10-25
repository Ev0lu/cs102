"""Vigenere Cipher"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword * (len(plaintext) // len(keyword) + 1)
    for symbol in range(len(plaintext)):
        symbol_num = ord(plaintext[symbol])
        shift = alphabet.index(keyword[symbol].lower())
        if plaintext[symbol].islower():
            ciphertext += alphabet[(symbol_num + shift - 97) % 26]
        elif plaintext[symbol].isupper():
            ciphertext += alphabet[(symbol_num + shift - 65) % 26].upper()
        else:
            ciphertext += plaintext[symbol]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword * (len(ciphertext) // len(keyword) + 1)
    for symbol in range(len(ciphertext)):
        symbol_num = ord(ciphertext[symbol])
        shift = alphabet.index(keyword[symbol].lower())
        if ciphertext[symbol].islower():
            plaintext += alphabet[(symbol_num - shift - 97) % 26]
        elif ciphertext[symbol].isupper():
            plaintext += alphabet[(symbol_num - shift - 65) % 26].upper()
        else:
            plaintext += ciphertext[symbol]
    return plaintext
