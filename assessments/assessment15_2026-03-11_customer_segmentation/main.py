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
