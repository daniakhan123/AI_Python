import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Sample dummy dataset (replace this with your actual student CSV)
data = {
    'student_id': range(1, 11),
    'GPA': [3.2, 2.8, 3.6, 2.4, 3.9, 3.1, 2.5, 3.7, 3.0, 2.9],
    'study_hours': [12, 8, 15, 5, 20, 11, 6, 18, 10, 9],
    'attendance_rate': [85, 70, 90, 60, 95, 80, 65, 92, 75, 72]
}

df = pd.DataFrame(data)

# ------------------------------
# Step 1: Feature Selection
# ------------------------------
features = ['GPA', 'study_hours', 'attendance_rate']
X = df[features]

# ------------------------------
# Step 2: Feature Scaling
# ------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------
# Step 3: Elbow Method to find optimal K
# ------------------------------
wcss = []
for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(6, 4))
plt.plot(range(2, 7), wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()
# ------------------------------
# Step 4: Apply KMeans with optimal K
# ------------------------------
optimal_k = 3
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans_final.fit_predict(X_scaled)

# ------------------------------
# Step 5: Visualization (Study Hours vs GPA)
# ------------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='study_hours', y='GPA', hue='cluster', palette='Set1', s=100)
plt.title("Student Clusters Based on GPA & Study Hours")
plt.xlabel("Average Weekly Study Hours")
plt.ylabel("GPA")
plt.legend(title='Cluster')
plt.grid(True)
plt.show()
# Show student_id and cluster assignments
final_output = df[['student_id', 'cluster']]
print(final_output)
