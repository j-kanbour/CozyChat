import random
from sympy import isprime

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi - 1)

    d = pow(e, -1, phi)

    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt(ciphertext, private_key):
    n, d = private_key
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

# Example usage:
public_key, private_key = generate_keypair(1024)
message = "Hello, RSA!"
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

print(f"Original message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
