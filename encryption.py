import os
import hashlib
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(file_data):
    generate_key()
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(file_data)
    return encrypted

def decrypt_file(encrypted_data):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_data)

def hash_file(file_data):
    return hashlib.sha256(file_data).hexdigest()