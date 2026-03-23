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
plt.pie(df["Marks"], labels=df["Subject"], autopct='%1.1f%%')
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
