import numpy as np
from sklearn.neighbors import NearestNeighbors

# User movie rating dataset
# Columns: Action, Comedy, Drama
ratings = np.array([
    [5, 2, 1],   # User1
    [4, 3, 1],   # User2
    [1, 5, 4],   # User3
])

model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(ratings)

distance, index = model.kneighbors([ratings[0]])

print("Nearest Users to User1:", index)
print("Distance:", distance)
print("\nUser1 is most similar to User", index[0][1] + 1)
