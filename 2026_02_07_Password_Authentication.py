import re

def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters"
    if not re.search("[A-Z]", password):
        return "Add at least one uppercase letter"
    if not re.search("[a-z]", password):
        return "Add at least one lowercase letter"
    if not re.search("[0-9]", password):
        return "Add at least one digit"
    if not re.search("[@#$%^&*]", password):
        return "Add at least one special character"
    return "Strong Password ✅"

pwd = input("Enter password: ")
print(check_password(pwd))
# Sample Output:
# Enter password: Abc@1234
# Strong Password ✅