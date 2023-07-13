from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from os import urandom
from getpass import getpass
from base64 import urlsafe_b64encode

# Derive a cryptographic key from the password

password_provided = getpass("Please enter your password: ")  # This should be replaced
password = password_provided.encode()  # Convert to type bytes
salt = urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = urlsafe_b64encode(kdf.derive(password))

# Encrypt the message
message = "my deep dark secret".encode()
f = Fernet(key)
encrypted = f.encrypt(message)
print(f"Encrypted message: {encrypted}")

# Decrypt the message
decrypted = f.decrypt(encrypted)
print(f"Decrypted message: {decrypted.decode()}")