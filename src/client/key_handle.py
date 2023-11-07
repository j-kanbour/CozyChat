from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import padding

def RSA_keygen():

    # Generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Commonly used value for public exponent
        key_size=2048,          # Choose your desired key size (e.g., 2048 bits)
    )

    # Serialize the private key and write it to a file (PEM format)
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('private_key.pem', 'wb') as private_key_file:
        private_key_file.write(private_key_pem)

    # Extract the public key from the private key
    public_key = private_key.public_key()

    # Serialize the public key and write it to a file (PEM format)
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('public_key.pem', 'wb') as public_key_file:
        public_key_file.write(public_key_pem)

    return public_key_pem

def RSA_encrypt(public_key, message):

    public_key = serialization.load_pem_private_key(public_key, password=None)

    encrypted_data = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=padding.ALGORITHMS.SHA256),
            algorithm=padding.ALGORITHMS.SHA256,
            label=None,
        )
    )
    return encrypted_data

def RSA_decrypt(private_key, message):
    #load private key
    with open('private_key.pem', 'rb') as private_key_file:
        private_key_data = private_key_file.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None)
    # Decrypt the data with the private key
    decrypted_data = private_key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=padding.ALGORITHMS.SHA256),
            algorithm=padding.ALGORITHMS.SHA256,
            label=None,
        )
    )

    return decrypted_data

def AES_keygen():
    # Generate a random AES key
    key = Fernet.generate_key()

    # Create an AES cipher with the key
    cipher = Fernet(key)

    return key, cipher

def AES_encrypt(cipher, message):

    # Encrypt the data
    encrypted_data = cipher.encrypt(message)

    return encrypted_data

def AES_decrypt(cipher, message):
    # Decrypt the data
    decrypted_data = cipher.decrypt(message)

    return decrypted_data.decode("utf-8")
