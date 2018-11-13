from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import mglearn
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
X = np.array([[1.5, 48], [1.5, 51], [1.6, 50], [1.65, 62], [1.70, 66], [1.80, 72]])
y = np.array([1, 1, 1, 0, 0, 0])
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X, y)
neigh.predict([[1.75, 68]])
s = [[0, 0, 0], [0, 0.5, 0], [1, 1, 5], [10, 10, 0]]
neigh1 = NearestNeighbors(n_neighbors=1)
neigh1.fit(s)
print(neigh1.kneighbors([[1, 0, 1], [9, 1, 3]]))