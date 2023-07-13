Python provides several libraries for performing cryptographic operations. One of the most commonly used is `cryptography`. Here's a simple example using Fernet symmetric key encryption from the `cryptography` module. Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.

```python
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
```

Please note the following about the above script:

- `getpass` is used for secure password input, where the input will not be echoed back.

- `os.urandom` is used to generate a cryptographically secure salt.

- A key derivation function (KDF) is used to generate a cryptographic key from the password. In this case, we're using PBKDF2 with HMAC and SHA256. The `derive` function performs the actual key derivation.

- Fernet symmetric encryption is used for actual message encryption and decryption.

Keep in mind that if you lose the key or password, the encrypted data is lost. Also, this script does not include the handling of the salt. If you restart the script, a new salt will be generated and you won't be able to decrypt your data. In a real application, you need to store the salt somewhere safe. 

Finally, although the script uses some of the best practices, encryption is a complex field and you should use a well-reviewed, established solution for any real-life, sensitive data. Always review and understand the documentation of cryptographic libraries, and if possible, consult with a security expert.