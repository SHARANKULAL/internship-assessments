import matplotlib.pyplot as plt

data = [10, 20, 30, 40]

plt.bar(["A","B","C","D"], data)
plt.show()

plt.pie(data, labels=["A","B","C","D"])
plt.show()

plt.hist(data)
plt.show()