
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
df = pd.read_csv('Mall_Customers.csv')

# Drop CustomerID and extract features
features = df.drop(columns='CustomerID')
X_all = features.values
kmeans_noscale = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels_noscale = kmeans_noscale.fit_predict(X_all)
# Separate Age column index
age_index = features.columns.get_loc('Age')

# Apply scaling to all features except 'Age'
X_scaled = X_all.copy()
scaler = StandardScaler()

# Scale all columns except Age
columns_to_scale = [i for i in range(X_all.shape[1]) if i != age_index]
X_scaled[:, columns_to_scale] = scaler.fit_transform(X_all[:, columns_to_scale])

kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

pca = PCA(n_components=2)

X_pca_noscale = pca.fit_transform(X_all)
X_pca_scaled = pca.fit_transform(X_scaled)

plt.figure(figsize=(12, 5))

# Without Scaling
plt.subplot(1, 2, 1)
plt.scatter(X_pca_noscale[:, 0], X_pca_noscale[:, 1], c=labels_noscale, cmap='rainbow')
plt.title("K-Means Clusters (No Scaling)")

# With Scaling (except Age)
plt.subplot(1, 2, 2)
plt.scatter(X_pca_scaled[:, 0], X_pca_scaled[:, 1], c=labels_scaled, cmap='rainbow')
plt.title("K-Means Clusters (Scaled except Age)")

plt.show()

