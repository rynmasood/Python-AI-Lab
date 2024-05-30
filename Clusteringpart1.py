import pandas as pd
import numpy as np
from sklearn.cluster import k_means
import matplotlib.pyplot as plt

def k_means(X, k, max_iterations=100):
   
    centroids = X[np.random.choice(range(X.shape[0]), size=k, replace=False)]
    
    for _ in range(max_iterations):
        
        labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=-1), axis=-1)
        
       
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
      
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return labels, centroids

data = pd.read_csv("feature.csv")


X = data.values


labels, centroids = k_means(X, k=3)
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Cluster Formation')
plt.show()

print("Labels:", labels)
print("Centroids:", centroids)