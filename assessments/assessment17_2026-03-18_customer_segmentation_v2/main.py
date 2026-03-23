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
