import password_hasher

hashed = password_hasher.hash_password("my_secure_password")
print(f"Hashed password: {hashed}")

is_valid = password_hasher.verify_password("my_secure_password", hashed)
print(f"Is valid (correct password): {is_valid}")

is_valid = password_hasher.verify_password("wrong_password", hashed)
print(f"Is valid (different password): {is_valid}")
