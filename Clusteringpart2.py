import pandas as pd
import numpy as np
from sklearn.cluster import k_means
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram,linkage
import matplotlib.pyplot as plt

data = pd.read_csv("Mall_Customers.csv")


X = data[['Annual Income (k$)', 'Spending Score (1-100)']]


kmeans = k_means(X, n_clusters=3)  
kmeans_labels = kmeans[1]  


agg_clustering = AgglomerativeClustering(n_clusters=3) 
agg_labels = agg_clustering.fit_predict(X)  


print("K-means labels:", kmeans_labels)
print("Agglomerative labels:", agg_labels)



linkage_matrix = linkage(X, method='ward')

plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=agg_labels, cmap='rainbow')

plt.show()

plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix)
plt.title('Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()