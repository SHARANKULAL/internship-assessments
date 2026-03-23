"""
Assessment Folder Generator
Generates structured folders for all internship assignments.
Run: python generate_assessments.py
"""

import os
import json
import re

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(BASE_PATH, "assessments")

# ─────────────────────────────────────────
# All 20 assessments
# ─────────────────────────────────────────
ASSESSMENTS = [
    {
        "n": 1,
        "date": "2026-02-07",
        "title": "Password Authentication",
        "code": '''\
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
    if not re.search(r\'[!@#$%^&*(),.?\\":{}|<>]\', password):
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
    print("User registered successfully!\\n")
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
''',
        "theory": """\
Assignment: Password Authentication (07/02/2026)

Security Features:
1. Password Hashing using SHA-256
   - hashlib.sha256 converts the password into a fixed-length hash.
   - Original password is never stored.

2. Random Salt
   - os.urandom(16) generates a random 16-byte salt each time.
   - Salt is combined with the password before hashing.
   - Prevents rainbow table attacks.

3. Strong Password Validation Rules
   - Minimum 8 characters
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one digit
   - At least one special character

4. No Plain-text Password Storage
   - Only the hash and salt are stored in memory.
"""
    },
    {
        "n": 2,
        "date": "2026-02-09",
        "title": "AI Around Me",
        "code": None,
        "theory": """\
Assignment: AI Around Me (09/02/2026)

10 Real-life AI Applications with ML Explanation:

1. Google Search
   Uses ML ranking algorithms to analyze keywords, user intent,
   and past behavior to show the most relevant results.

2. YouTube Recommendations
   ML models track watch history, likes, and watch time to
   recommend personalized videos.

3. Smartphone Face Unlock
   Uses deep learning to extract facial features and match them
   with stored biometric data.

4. Google Maps Navigation
   ML predicts traffic and optimal routes using real-time
   location data and historical patterns.

5. Voice Assistants (Google Assistant / Alexa)
   Speech recognition and NLP models convert voice to text
   and understand intent.

6. Email Spam Filter (Gmail)
   ML classifiers detect spam by learning from email content,
   sender behavior, and user feedback.

7. Netflix Recommendations
   Collaborative filtering ML models suggest movies based on
   viewing patterns of similar users.

8. Online Shopping Suggestions (Amazon / Flipkart)
   ML analyzes browsing history and purchases to recommend products.

9. Social Media Feed (Instagram / Facebook)
   ML ranks posts by predicting user engagement like clicks,
   likes, and shares.

10. Phone Keyboard Autocorrect & Prediction
    Language models learn from typing patterns to predict the
    next word and correct errors.
"""
    },
    {
        "n": 3,
        "date": "2026-02-12",
        "title": "Smart Input Program",
        "code": '''\
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

print("\\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {age} years old and belong to the category: {category}.")
print(f"It\'s great that you enjoy {hobby}. Keep pursuing it!")
''',
        "theory": """\
Assignment: Smart Input Program (12/02/2026)

How It Works:
- Takes input: name, age, hobby
- Uses if-elif-else conditionals to categorize age

Age Categories:
  < 13        → Child
  13 to 19    → Teenager
  20 to 59    → Adult
  60+         → Senior Citizen

- Prints a personalized output message combining all inputs.
"""
    },
    {
        "n": 4,
        "date": "2026-02-12",
        "title": "FizzBuzz",
        "code": '''\
# FizzBuzz Program (1-50) with Count

def check_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def run_fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = check_fizzbuzz(i)
        print(result)
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1

    print("\\n--- Count Summary ---")
    print("Fizz Count:", fizz_count)
    print("Buzz Count:", buzz_count)
    print("FizzBuzz Count:", fizzbuzz_count)

run_fizzbuzz()
''',
        "theory": """\
Assignment: FizzBuzz (12/02/2026)

Logic:
- If number divisible by 3   → print "Fizz"
- If divisible by 5          → print "Buzz"
- If divisible by both 3 & 5 → print "FizzBuzz"
- Otherwise                  → print the number

Using:
- One function for logic (check_fizzbuzz)
- One function for execution & counting (run_fizzbuzz)
- for loop from 1 to 50
"""
    },
    {
        "n": 5,
        "date": "2026-02-19",
        "title": "Student Data Manager",
        "code": '''\
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
    print(f"Name: {student[\'name\']}, Marks: {student[\'marks\']}, Grade: {grade}")

print("\\nTopper:", topper["name"], "with", topper["marks"], "marks")
print("Class Average:", round(class_average, 2))
''',
        "theory": """\
Assignment: Student Data Manager (19/02/2026)

Program Features:
- Stores student data using dictionary of dictionaries
- Uses a function to assign grades based on marks
- Calculates class average using sum and len
- Finds topper using max() with lambda

Grade Scale:
  >= 90 → A
  >= 75 → B
  >= 60 → C
  >= 40 → D
  <  40 → F
"""
    },
    {
        "n": 6,
        "date": "2026-02-20",
        "title": "NumPy Speed Test",
        "code": '''\
import time
import numpy as np

size = 1_000_000

python_list = list(range(size))
numpy_array = np.arange(size)

# Python List
start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy Array
start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print("Execution Time (Python List):", python_time, "seconds")
print("Execution Time (NumPy Array):", numpy_time, "seconds")
print("Speed Difference:", python_time - numpy_time, "seconds")
''',
        "theory": """\
Assignment: NumPy Speed Test (20/02/2026)

3 Observations:
1. NumPy executes significantly faster because it uses vectorized
   operations implemented in optimized C code.

2. Python lists require explicit looping, which introduces
   interpreter overhead and increases execution time.

3. NumPy is better suited for large-scale numerical computations,
   making it ideal for machine learning, data science, and
   scientific computing tasks.
"""
    },
    {
        "n": 7,
        "date": "2026-02-24",
        "title": "Dataset Detective",
        "code": '''\
import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("----- Top 5 Rows -----")
print(df.head())

max_values = df.max(numeric_only=True)
highest_column = max_values.idxmax()
highest_value = max_values.max()

print("\\nColumn with Highest Maximum Value:")
print("Column:", highest_column)
print("Value:", highest_value)

print("\\n----- Missing Values -----")
print(df.isnull().sum())

print("\\n----- Statistical Summary -----")
print(df.describe())
''',
        "theory": """\
Assignment: Dataset Detective (24/02/2026)

Explanation:
- read_csv()        → Loads dataset into DataFrame
- head()            → Displays first 5 rows
- max() + idxmax()  → Finds column with highest maximum value
- isnull().sum()    → Counts missing values
- describe()        → Shows mean, std, min, max etc.

5 Insights:
1. The dataset contains both numerical and categorical features.
2. The column with the highest value indicates the largest
   recorded observation in the dataset.
3. Some columns contain missing values requiring data cleaning.
4. Mean and median comparison helps identify skewness in data.
5. High standard deviation in certain columns suggests
   large variability.
"""
    },
    {
        "n": 8,
        "date": "2026-02-26",
        "title": "Data Doctor",
        "code": '''\
import pandas as pd

df = pd.read_csv("dataset.csv")

print("Original Dataset:")
print(df.head())

# 1. Handle Missing Values
df = df.ffill()

# 2. Remove Duplicate Rows
df = df.drop_duplicates()

# 3. Standardize Text
df.columns = df.columns.str.strip().str.lower()

for col in df.select_dtypes(include=\'object\'):
    df[col] = df[col].str.strip().str.lower()

print("\\nCleaned Dataset:")
print(df.head())

df.to_csv("cleaned_dataset.csv", index=False)
print("\\nCleaned dataset saved as cleaned_dataset.csv")
''',
        "theory": """\
Assignment: Data Doctor (26/02/2026)

Cleaning Steps:
1. Handle Missing Values
   - ffill() fills missing values with the previous available value.

2. Remove Duplicates
   - drop_duplicates() removes repeated records.

3. Standardize Text
   - Columns converted to lowercase.
   - Extra spaces stripped using str.strip().

Why Data Cleaning Matters:
- Improves data quality for accurate analysis.
- Prevents incorrect results from duplicates or nulls.
- Makes data consistent for ML models.
- Improves model performance.
- Saves time during analysis.
"""
    },
    {
        "n": 9,
        "date": "2026-02-28",
        "title": "Storytelling with Graphs",
        "code": '''\
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Subject": ["Math", "Science", "English", "History", "Computer"],
    "Marks":   [85, 90, 78, 70, 95]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure()
plt.bar(df["Subject"], df["Marks"], color="steelblue")
plt.title("Marks by Subject (Bar Chart)")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Pie Chart
plt.figure()
plt.pie(df["Marks"], labels=df["Subject"], autopct=\'%1.1f%%\')
plt.title("Marks Distribution (Pie Chart)")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"], bins=5, color="coral", edgecolor="black")
plt.title("Marks Distribution (Histogram)")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()
''',
        "theory": """\
Assignment: Storytelling with Graphs (28/02/2026)

Data Story:
The visualizations show the distribution of marks across
different subjects.

- Bar Chart: Computer and Science have the highest scores;
  History has the lowest performance.

- Pie Chart: A larger percentage of total marks comes from
  Computer and Science subjects.

- Histogram: Most marks fall between 75 and 95, indicating
  generally good academic performance with few low scores.
"""
    },
    {
        "n": 10,
        "date": "2026-03-02",
        "title": "ML Idea Generator",
        "code": None,
        "theory": """\
Assignment: ML Idea Generator (02/03/2026)

ML Problems and Input → Output Descriptions:

College:
1. Student Performance Prediction
   Input  → Attendance, study hours, previous marks, assignments
   Output → Predicted final exam score or pass/fail result

2. Attendance Monitoring System
   Input  → Classroom images or face data
   Output → Automatic attendance list

Healthcare:
3. Disease Prediction System
   Input  → Patient symptoms, age, medical history, test results
   Output → Predicted disease risk or diagnosis

4. Heart Attack Risk Prediction
   Input  → Blood pressure, cholesterol, ECG, age, lifestyle
   Output → Probability of heart attack risk

Shopping:
5. Product Recommendation System
   Input  → Browsing history, purchase history, ratings
   Output → Personalized product recommendations

6. Price Prediction System
   Input  → Product category, brand, demand, past prices
   Output → Predicted optimal product price
"""
    },
    {
        "n": 11,
        "date": "2026-03-03",
        "title": "Build Your First Dataset",
        "code": '''\
import pandas as pd

# Load dataset
df = pd.read_csv("study_hours_marks.csv")

print("Dataset:")
print(df)

print("\\nCorrelation between Study Hours and Marks:")
print(df.corr(numeric_only=True))

print("\\nMean Study Hours:", df["Study_Hours"].mean())
print("Mean Marks:", df["Marks"].mean())
''',
        "theory": """\
Assignment: Build Your First Dataset (03/03/2026)

Dataset: Study Hours vs Marks

Feature (Input) : Study_Hours
Label (Output)  : Marks

Relationship:
There is a positive relationship between study hours and marks.
As the number of study hours increases, marks also increase.
This can be modeled using Linear Regression.

CSV Data:
Study_Hours,Marks
1,40
2,45
3,50
4,55
5,65
6,70
7,78
8,85
9,92
10,96
""",
        "csv": "Study_Hours,Marks\n1,40\n2,45\n3,50\n4,55\n5,65\n6,70\n7,78\n8,85\n9,92\n10,96\n"
    },
    {
        "n": 12,
        "date": "2026-03-07",
        "title": "KNN in Real Life",
        "code": '''\
import numpy as np
from sklearn.neighbors import NearestNeighbors

# User movie rating dataset
# Columns: Action, Comedy, Drama
ratings = np.array([
    [5, 2, 1],   # User1
    [4, 3, 1],   # User2
    [1, 5, 4],   # User3
])

model = NearestNeighbors(n_neighbors=2, metric=\'euclidean\')
model.fit(ratings)

distance, index = model.kneighbors([ratings[0]])

print("Nearest Users to User1:", index)
print("Distance:", distance)
print("\\nUser1 is most similar to User", index[0][1] + 1)
''',
        "theory": """\
Assignment: KNN in Real Life (07/03/2026)

Netflix-like Recommendation using KNN:
- KNN finds K most similar users (nearest neighbors).
- Recommends movies liked by neighbors but not yet seen
  by the current user.

Example:
  User1 and User2 both liked Action & Sci-Fi movies.
  If User2 watches a new Action movie, it gets recommended
  to User1.

Rating Table:
| User  | Action | Comedy | Drama |
|-------|--------|--------|-------|
| User1 |   5    |   2    |   1   |
| User2 |   4    |   3    |   1   |
| User3 |   1    |   5    |   4   |

Conclusion:
KNN is used in movie/music streaming, online shopping,
and content filtering systems.
"""
    },
    {
        "n": 13,
        "date": "2026-03-09",
        "title": "House Price Predictor",
        "code": '''\
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Size_sqft": [500, 800, 1000, 1200, 1500],
    "Price":     [1000000, 1600000, 2000000, 2400000, 3000000]
}

df = pd.DataFrame(data)

X = df[["Size_sqft"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

predicted_prices = model.predict(X)

print("Predicted Prices:")
for size, price in zip(df["Size_sqft"], predicted_prices):
    print(f"House size: {size} sqft -> Predicted Price: {round(price, 2)}")

new_house_size = [[1100]]
predicted_price = model.predict(new_house_size)

print("\\nPrediction for new house:")
print(f"House size: 1100 sqft -> Estimated Price: {round(predicted_price[0], 2)}")
''',
        "theory": """\
Assignment: House Price Predictor (09/03/2026)

Explanation:
1. Dataset contains house size (sqft) and price.
2. Size_sqft is the feature (input); Price is the label (output).
3. Linear Regression learns the relationship between size and price.
4. Trained model predicts prices for known data.
5. New house size (1100 sqft) is given to estimate price.

Result:
As house size increases, price also increases — showing a
positive linear relationship.
"""
    },
    {
        "n": 14,
        "date": "2026-03-10",
        "title": "Spam Classifier Thinking",
        "code": None,
        "theory": """\
Assignment: Spam Classifier Thinking (10/03/2026)

1. Features Used for Spam Detection:
   - Word Frequency: "free", "win", "offer", "click here"
   - Sender Information: unknown or suspicious email addresses
   - Number of Links: spam often has many links
   - Special Characters: !!!, $, %
   - Message Length: unusually short or long promotional messages
   - Capitalization: "WIN MONEY NOW"

2. Data Needed:
   - Email or SMS text content
   - Label: Spam or Not Spam (Ham)
   - Sender information
   - Time and frequency of messages
   - Large historical labeled dataset

   Example:
   | Message                          | Label    |
   |----------------------------------|----------|
   | Win a free iPhone now            | Spam     |
   | Meeting at 3 PM today            | Not Spam |
   | Limited time offer click here    | Spam     |

3. Possible Mistakes:
   - False Positive: Normal message wrongly classified as spam
   - False Negative: Spam message appears in inbox
   - Language Variations: Misspellings to bypass filters
   - Evolving Spam Techniques
   - Limited Training Data reduces accuracy

Conclusion:
ML classifiers with proper feature selection and large labeled
datasets help improve accuracy and reduce mistakes.
"""
    },
    {
        "n": 15,
        "date": "2026-03-11",
        "title": "Customer Segmentation",
        "code": '''\
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Annual_Income":  [15, 16, 17, 40, 42, 43, 70, 72, 75, 90, 95, 100],
    "Spending_Score": [39, 40, 42, 60, 61, 65, 20, 22, 25, 80, 85, 88],
}

df = pd.DataFrame(data)

X = df[["Annual_Income", "Spending_Score"]]

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

print(df)

plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap="viridis")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.show()
''',
        "theory": """\
Assignment: Customer Segmentation (11/03/2026)

Description of Customer Groups after K-Means clustering:

1. Low Income – Low Spending Group
   Customers with small income and low spending score.
   They are budget customers.

2. Medium Income – Medium Spending Group
   Customers with average income and moderate spending.
   They are regular customers.

3. High Income – High Spending Group
   Customers with high income and high spending score.
   They are premium customers, important for business.

Conclusion:
K-Means clustering helps businesses understand different types
of customers and create targeted marketing strategies.
"""
    },
    {
        "n": 16,
        "date": "2026-03-12",
        "title": "Decision Tree on Paper",
        "code": None,
        "theory": """\
Assignment: Decision Tree on Paper (12/03/2026)

Decision Tree: Should I Play Outside?

                    Weather
                  /    |     \\
              Sunny   Rainy  Cloudy
               /        |        \\
         Homework?      No    Temperature
          /     \\              /       \\
        Yes      No          Hot      Cool
         |        |           |         |
        No       Yes          No        Yes


Explanation:
- First condition: Weather
    - Rainy → Do NOT play
    - Sunny → Check Homework
        - Homework = Yes → Do NOT play
        - Homework = No  → PLAY
    - Cloudy → Check Temperature
        - Hot  → Do NOT play
        - Cool → PLAY

Conclusion:
A decision tree helps make decisions step-by-step using
conditions. Used in ML for classification and prediction.
"""
    },
    {
        "n": 17,
        "date": "2026-03-18",
        "title": "Customer Segmentation v2",
        "code": '''\
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Annual_Income":  [15, 18, 20, 35, 40, 45, 60, 65, 70, 85, 90, 95],
    "Spending_Score": [39, 42, 40, 60, 65, 63, 25, 30, 28, 80, 85, 90],
}

df = pd.DataFrame(data)

X = df[["Annual_Income", "Spending_Score"]]

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

print(df)

plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap="plasma")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means (v2)")
plt.tight_layout()
plt.savefig("customer_clusters_v2.png")
plt.show()
''',
        "theory": """\
Assignment: Customer Segmentation v2 (18/03/2026)

Description of Customer Groups:

1. Low Income – Low Spending Customers
   Less income and less spending. Budget buyers.

2. Medium Income – Medium Spending Customers
   Average income and normal spending. Regular customers.

3. High Income – High Spending Customers
   Earn more and spend more. Premium customers.
   Important for business marketing.

Conclusion:
Customer segmentation using K-Means helps businesses understand
customer behavior and create better offers for each group.
"""
    },
    {
        "n": 18,
        "date": "2026-03-19",
        "title": "Mini Project Proposal",
        "code": None,
        "theory": """\
Assignment: Mini Project Proposal (19/03/2026)
Title: Student Performance Prediction using Machine Learning

1. Problem Statement:
   In colleges, it is difficult to identify whether a student
   will perform well in exams. This project aims to predict
   student performance using ML so teachers can identify
   weak students early and provide support.

2. Dataset:
   Columns: StudyHours, Attendance, PreviousMarks,
            Assignment, SleepHours, FinalMarks
   Source: Manual CSV or online dataset.

3. Algorithm Used:
   - Linear Regression  → to predict marks
   - Logistic Regression → to predict pass/fail

4. Expected Output:
   - Predicted student marks based on input data.
   - Probability of pass or fail.
   - Dashboard for teachers to monitor performance.

5. Conclusion:
   Demonstrates how ML can be used in education to analyze
   student data and make early predictions.
"""
    },
    {
        "n": 19,
        "date": "2026-03-20",
        "title": "Text Challenges",
        "code": None,
        "theory": """\
Assignment: Text Challenges (20/03/2026)

20 Messy Sentences:
1.  hey brooo what r u doin
2.  omg this moviee sooo gud!!!
3.  I canttt believe this
4.  lol that was funnyyyy
5.  gm frnd how r u
6.  I luv this song
7.  y r u late???
8.  this is amazng
9.  okkkk I will cm tmrw
10. thx bro
11. wat is ur plan 2day
12. noooo dont do that
13. I am soooo tired
14. u coming or not??
15. thats gr8 news
16. pls send d file
17. hahaha this is crazyyy
18. I didnt get it
19. meet me @ 5pm
20. gud nyt tc

Issues Found:
| Issue           | Example                    |
|-----------------|----------------------------|
| Slang           | bro, gm, gr8, pls          |
| Emojis          | removed for NLP            |
| Typos           | moviee, amazng, doin       |
| Short forms     | u, r, wat, ur, 2day        |
| Extra letters   | sooo, funnyyyy, noooo      |
| Symbols         | @, ???, !!!                |

Preprocessing Needed:
1. Convert to lowercase
2. Remove emojis
3. Correct spelling / remove repeated letters
4. Expand short forms and slang
5. Remove special characters
6. Tokenization
7. Stopword removal (optional)

Conclusion:
Text preprocessing is essential in NLP. Clean text improves
machine learning accuracy and analysis quality.
"""
    },
    {
        "n": 20,
        "date": "2026-03-21",
        "title": "Build a Text Cleaner",
        "code": '''\
import string

stopwords = [
    "is", "am", "are", "the", "a", "an", "and",
    "to", "in", "of", "for", "on", "at", "this",
    "it", "that", "was", "were"
]

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Remove stopwords
    filtered_words = [word for word in words if word not in stopwords]

    cleaned_text = " ".join(filtered_words)
    return cleaned_text


# Test the cleaner
test_sentences = [
    "Hello!!! This is a Simple TEXT cleaning program.",
    "The Quick Brown Fox Jumps Over the Lazy Dog.",
    "Python is great for Data Science and Machine Learning!",
]

for sentence in test_sentences:
    print("Original:", sentence)
    print("Cleaned :", clean_text(sentence))
    print()
''',
        "theory": """\
Assignment: Build a Text Cleaner (21/03/2026)

What This Code Does:
1. Converts text to lowercase
2. Removes punctuation marks using str.maketrans
3. Splits sentence into words
4. Removes stopwords from a predefined list
5. Joins filtered words back into a sentence

Example Output:
  Original: Hello!!! This is a Simple TEXT cleaning program.
  Cleaned : hello simple text cleaning program

Why This Matters:
Text cleaning is a fundamental step in NLP preprocessing
pipelines. Clean text improves ML model training quality
and reduces noise in feature extraction.
"""
    },
]


# ─────────────────────────────────────────
# Helper functions
# ─────────────────────────────────────────
def sanitize(name):
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name or "untitled"


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ─────────────────────────────────────────
# Main generator
# ─────────────────────────────────────────
def generate():
    os.makedirs(ROOT, exist_ok=True)
    manifest = []

    for a in ASSESSMENTS:
        folder_name = f"assessment{a['n']}_{a['date']}_{sanitize(a['title'])}"
        folder_path = os.path.join(ROOT, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # main.py
        if a.get("code"):
            write(os.path.join(folder_path, "main.py"), a["code"])

        # theory.txt
        if a.get("theory"):
            write(os.path.join(folder_path, "theory.txt"), a["theory"])

        # CSV (only for dataset assessment)
        if a.get("csv"):
            write(os.path.join(folder_path, "study_hours_marks.csv"), a["csv"])

        manifest.append({
            "assessment": a["n"],
            "date": a["date"],
            "title": a["title"],
            "folder": folder_path,
        })

        print(f"[{a['n']:02d}] Created: {folder_name}")

    manifest_path = os.path.join(ROOT, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)

    print(f"\nDone! {len(manifest)} assessments generated.")
    print(f"Manifest saved: {manifest_path}")


if __name__ == "__main__":
    generate()
