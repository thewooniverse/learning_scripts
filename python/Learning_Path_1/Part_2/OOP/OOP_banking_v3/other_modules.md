

============================================================================================================
DATETIME
============================================================================================================
Certainly! The `datetime` module in Python deals with dates and times. It provides classes for manipulating dates, times, time intervals, and time-aware objects. Here are the basics of the `datetime` module:

1. **Imports**:
   ```python
   import datetime
   ```

2. **Important Classes**:

   - `datetime.date`: Represents a date (year, month, day).
   - `datetime.time`: Represents a time of day (hour, minute, second, microsecond).
   - `datetime.datetime`: Represents a date and time.
   - `datetime.timedelta`: Represents a duration or difference between two dates/times.
   - `datetime.tzinfo`: Base class for time zones.

3. **Getting Current Date and Time**:

   - Current date:
     ```python
     today = datetime.date.today()
     print(today)  # Example output: 2023-07-07
     ```

   - Current date and time:
     ```python
     now = datetime.datetime.now()
     print(now)  # Example output: 2023-07-07 14:55:02.558
     ```

4. **Creating Date and Time Objects**:

   ```python
   d = datetime.date(2023, 7, 7)
   t = datetime.time(14, 55, 2)
   dt = datetime.datetime(2023, 7, 7, 14, 55, 2)
   ```

5. **Time Delta (Duration between times)**:

   ```python
   delta = datetime.timedelta(days=7, hours=3)
   future_date = today + delta
   past_date = today - delta
   ```

6. **Formatting Dates and Times**:

   - Convert a datetime object to a string with a specific format:
     ```python
     formatted = now.strftime('%Y-%m-%d %H:%M:%S')
     print(formatted)  # Example output: '2023-07-07 14:55:02'
     ```

   - Parse a string into a datetime object:
     ```python
     dt_str = '2023-07-07 14:55:02'
     parsed_dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
     ```

7. **Attributes and Methods**:

   - Access individual components:
     ```python
     year = today.year
     month = today.month
     day = today.day
     ```

   - Replace components:
     ```python
     new_dt = dt.replace(year=2025)
     ```

   - Compute the difference between two datetime objects:
     ```python
     diff = dt1 - dt2  # This returns a timedelta object.
     ```

   - Weekday (Monday is 0 and Sunday is 6):
     ```python
     weekday_num = today.weekday()
     ```

   - ISO format:
     ```python
     iso_format = today.isoformat()
     ```

8. **Time Zone Handling**:
   
   The `datetime` module has limited support for time zones. For comprehensive time zone handling, consider using the third-party library `pytz`.

   ```python
   import pytz

   # Localize datetime to a timezone
   tz = pytz.timezone('US/Eastern')
   eastern_time = tz.localize(datetime.datetime.now())

   # Convert datetime to another timezone
   utc_time = eastern_time.astimezone(pytz.utc)
   ```

These are the basics of the `datetime` module in Python. It's a comprehensive module, and there's a lot you can do with it, but these fundamental concepts will get you started on most tasks involving dates and times.




============================================================================================================
ENCRYPTION
============================================================================================================
ENCRYPTION MODULE NOTES:

Encrypting a file using a PIN or password can be accomplished using a variety of cryptographic libraries in Python. One of the simpler and well-known libraries for this purpose is `cryptography`. 


Here's a basic example of how to encrypt a file using a PIN (like "1234") using the `cryptography` library:

1. First, install the necessary library:

```bash
pip install cryptography
```

2. Next, use this Python script to encrypt and decrypt a file:

```python
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
import os

def key_from_pin(pin: str, salt: bytes) -> bytes:
    """Generate a Fernet key using a PIN and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(pin.encode()))
    return key

def encrypt_file(file_path: str, pin: str):
    """Encrypt a file using a PIN."""
    salt = os.urandom(16)  # Random salt for encryption
    key = key_from_pin(pin, salt)
    cipher = Fernet(key)

    # Read the file and encrypt its content
    with open(file_path, 'rb') as f:
        encrypted_data = cipher.encrypt(f.read())

    # Write the salt and the encrypted content to a new file
    with open(file_path + ".encrypted", 'wb') as f:
        f.write(salt + encrypted_data)

def decrypt_file(encrypted_file_path: str, pin: str, output_file_path: str):
    """Decrypt a file using a PIN."""
    with open(encrypted_file_path, 'rb') as f:
        data = f.read()
    salt, encrypted_data = data[:16], data[16:]  # Extract salt and encrypted content

    key = key_from_pin(pin, salt)
    cipher = Fernet(key)
    
    # Decrypt the content and write it to the output file
    with open(output_file_path, 'wb') as f:
        f.write(cipher.decrypt(encrypted_data))

# Example Usage:
# encrypt_file("sample.txt", "1234")
# decrypt_file("sample.txt.encrypted", "1234", "decrypted_sample.txt")
```

This script defines functions to encrypt and decrypt a file using a given PIN. It uses a key derivation function (`PBKDF2HMAC`) to generate a secure key from your PIN, and then uses that key to encrypt/decrypt the file content.

Remember: Although using a PIN like "1234" is easy for demonstration purposes, in real-world applications, always use strong, unique passwords to ensure the security of your encrypted data.




