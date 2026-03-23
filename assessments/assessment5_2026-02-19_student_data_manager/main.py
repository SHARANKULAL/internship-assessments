# Student Data Manager

def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

students = {
    "S1": {"name": "Rahul",  "marks": 85},
    "S2": {"name": "Ananya", "marks": 92},
    "S3": {"name": "Vikram", "marks": 74},
    "S4": {"name": "Sneha",  "marks": 66},
    "S5": {"name": "Arjun",  "marks": 58},
}

total_marks = sum(s["marks"] for s in students.values())
class_average = total_marks / len(students)
topper = max(students.values(), key=lambda x: x["marks"])

print("----- Student Report -----")
for student in students.values():
    grade = assign_grade(student["marks"])
    print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {grade}")

print("\nTopper:", topper["name"], "with", topper["marks"], "marks")
print("Class Average:", round(class_average, 2))
