import numpy as np
import pandas as pd


X = np.random.randint(10, 50, 100).reshape(10, 10)

mean = np.mean(X, axis=0)
print("Mean of each feature:")
print(mean)

X_centered = X - mean
print("Centered data:")
print(X_centered)

covariance_matrix = np.cov(X_centered.T)
print("Covariance matrix:")
print(covariance_matrix)

eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)


sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
print("Sorted eigenvalues:")
print(sorted_eigenvalues)
print("Sorted eigenvectors:")
print(sorted_eigenvectors)


k = 2  
selected_eigenvectors = sorted_eigenvectors[:, :k]
print("Selected eigenvectors:")
print(selected_eigenvectors)


transformed_data = np.dot(X_centered, selected_eigenvectors)
print("Transformed data:")
print(transformed_data)



