import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fixing quote issues and creating DataFrame
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)

# Drop 'vehicle_serial_no' as it's just an ID
df_clustering = df.drop(columns='vehicle_serial_no')
# One-hot encode vehicle_type for fair clustering
df_noscale = pd.get_dummies(df_clustering, columns=['vehicle_type'], drop_first=True)

# Apply KMeans
kmeans_noscale = KMeans(n_clusters=3, random_state=42)
labels_noscale = kmeans_noscale.fit_predict(df_noscale)
df_noscale['Cluster'] = labels_noscale
# Separate features
num_features = ['mileage', 'fuel_efficiency', 'maintenance_cost']
cat_features = ['vehicle_type']

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(drop='first'), cat_features)
])

# Full pipeline
pipeline_scaled = Pipeline([
    ('preprocess', preprocessor),
    ('kmeans', KMeans(n_clusters=3, random_state=42))
])

# Fit and predict
pipeline_scaled.fit(df_clustering)
labels_scaled = pipeline_scaled.named_steps['kmeans'].labels_
df_scaled = df.copy()
df_scaled['Cluster'] = labels_scaled
print("Without Scaling:\n", df_noscale['Cluster'].value_counts())
print("\nWith Scaling:\n", df_scaled['Cluster'].value_counts())
# Use mileage vs fuel_efficiency to visualize clusters
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.scatterplot(data=df_noscale, x='mileage', y='fuel_efficiency', hue='Cluster', palette='Set1')
plt.title("Without Scaling")

plt.subplot(1,2,2)
sns.scatterplot(data=df_scaled, x='mileage', y='fuel_efficiency', hue='Cluster', palette='Set2')
plt.title("With Scaling")

plt.tight_layout()
plt.show()
