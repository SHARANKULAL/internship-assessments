name = input("Enter name: ")
age = int(input("Enter age: "))
hobby = input("Enter hobby: ")

if age < 18:
    category = "Teen"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"Hello {name}! You are an {category} who loves {hobby}.")


#output 
#Enter name: Chinmayee d
#Enter age: 22
#Enter hobby: singing
#Hello Chinmayee d! You are an Adult who loves singing.