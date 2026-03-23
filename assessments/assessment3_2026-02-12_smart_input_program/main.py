# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "Child"
elif age >= 13 and age < 20:
    category = "Teenager"
elif age >= 20 and age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {age} years old and belong to the category: {category}.")
print(f"It's great that you enjoy {hobby}. Keep pursuing it!")
