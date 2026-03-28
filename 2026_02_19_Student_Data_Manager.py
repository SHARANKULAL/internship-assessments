students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 70},
    {"name": "D", "marks": 85},
    {"name": "E", "marks": 60}
]

total = sum(s["marks"] for s in students)
avg = total / len(students)

topper = max(students, key=lambda x: x["marks"])

def grade(m):
    if m >= 85: return "A"
    elif m >= 70: return "B"
    else: return "C"

print("Topper:", topper)
print("Average:", avg)

for s in students:
    print(s["name"], "Grade:", grade(s["marks"]))