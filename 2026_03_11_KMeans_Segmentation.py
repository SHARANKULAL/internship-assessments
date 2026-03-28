from sklearn.cluster import KMeans
import numpy as np

data = np.array([[10],[20],[30],[100],[110]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print(kmeans.labels_)