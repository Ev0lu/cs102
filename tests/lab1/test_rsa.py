"""Test the rsa module"""


from src.lab2.rsa import gcd
from src.lab2.rsa import generate_keypair, is_prime, multiplicative_inverse


def test_is_prime():
    # Test case 1: prime number
    assert is_prime(2) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True

    # Test case 2: composite number
    assert is_prime(4) == False
    assert is_prime(8) == False
    assert is_prime(10) == False
    assert is_prime(15) == False

    # Test case 3: edge cases
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-2) == False


def test_multiplicative_inverse():
    # Test case 1: e and phi are coprime
    e = 7
    phi = 40
    assert multiplicative_inverse(e, phi) == 23

    # Test case 2: e and phi are not coprime
    e = 6
    phi = 40
    try:
        multiplicative_inverse(e, phi)
    except ValueError as e:
        assert str(e) == "e and phi must be coprime."

    # Test case 3: phi is greater than e
    e = 7
    phi = 50
    assert multiplicative_inverse(e, phi) == 43


def test_gcd():
    # Test case 1: gcd of two prime numbers
    assert gcd(5, 7) == 1
    assert gcd(11, 13) == 1

    # Test case 2: gcd of two composite numbers
    assert gcd(4, 6) == 2
    assert gcd(8, 12) == 4

    # Test case 3: gcd of a prime and a composite number
    assert gcd(3, 10) == 1
    assert gcd(7, 14) == 7

    # Test case 4: gcd of a number and itself
    assert gcd(5, 5) == 5
    assert gcd(10, 10) == 10

    # Test case 5: gcd of a number and 0
    assert gcd(5, 0) == 5
    assert gcd(0, 10) == 10
