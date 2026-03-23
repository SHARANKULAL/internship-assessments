import hashlib
import os
import re

# ---------- Password Strength Checker ----------
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return False
    return True

# ---------- Password Hashing ----------
def hash_password(password, salt):
    return hashlib.sha256(salt + password.encode()).hexdigest()

# ---------- User Registration ----------
def register_user():
    username = input("Enter username: ")
    password = input("Create password: ")
    if not is_strong_password(password):
        print("Password not strong enough!")
        print("Must be 8+ chars, upper, lower, digit & special char")
        return None
    salt = os.urandom(16)
    hashed_password = hash_password(password, salt)
    print("User registered successfully!\n")
    return {"username": username, "salt": salt, "password_hash": hashed_password}

# ---------- User Login ----------
def login_user(stored_user):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username != stored_user["username"]:
        print("Invalid username")
        return
    hashed_input = hash_password(password, stored_user["salt"])
    if hashed_input == stored_user["password_hash"]:
        print("Login successful!")
    else:
        print("Incorrect password")

# ---------- Main ----------
print("=== PASSWORD AUTHENTICATION SYSTEM ===")
user_data = register_user()
if user_data:
    print("=== LOGIN ===")
    login_user(user_data)
