from encryption import encrypt_file, decrypt_file, hash_file

data = b"This is a secret patient record."
encrypted = encrypt_file(data)
decrypted = decrypt_file(encrypted)
file_hash = hash_file(data)

print("Original:  ", data)
print("Encrypted: ", encrypted[:50], "...")
print("Decrypted: ", decrypted)
print("SHA-256:   ", file_hash)
print("\n✅ Encryption working!" if data == decrypted else "\n❌ Something went wrong")