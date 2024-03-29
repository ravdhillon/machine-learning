import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from matplotlib import style
style.use('ggplot')

X = np.array([[1,2],
            [1.5, 1.8],
            [5, 8],
            [8, 8],
            [1, 0.6],
            [9, 11]])
plt.scatter(X[:, 0], X[:, 1], s=150, linewidths=5)
plt.show()

colors = 10 * ["g", "r", "c", "b", "k", "o"]


# Define the KMeans class
class K_Means:
    '''
        k = clusters
        tolerance = movement of the cluster
    '''
    def __init__(self, k=2, tolerance=0.001, max_iter=300):
        self.k = k
        self.tolerance = tolerance
        self.max_iter = max_iter

    
    def fit(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]
        
        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []
            
            # X is data
            for featureset in X:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroid = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0) #finding mean of any given class
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroid[c]
                current_centroid = self.centroids[c]

                if np.sum((current_centroid - original_centroid)/original_centroid * 100) > self.tolerance:
                    optimized = False
            if optimized:
                break
        
    def predict(self, data):
        distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

clf = K_Means()
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], 
        marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)

plt.show()
