import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn.metrics import classification_report, accuracy_score
df = pd.read_csv('customers.csv')  # replace with your file name
print(df.head())
print(df.info())
print(df.isnull().sum())
df.fillna(df.median(numeric_only=True), inplace=True)
X = df[['Total_Spending_6mo', 'Age', 'Num_Visits', 'Purchase_Frequency']]
y = df['Customer_Value']  # 1 = High, 0 = Low
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = SVC(kernel='linear')  # Linear SVM for a hyperplane
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
model = SVC(kernel='linear')  # Linear SVM for a hyperplane
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
