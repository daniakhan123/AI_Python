# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
new_emails = [
    "Win a free iPhone! Click here to claim your prize now!",
    "Hi team, please find attached the report for last week."
]

predictions = model.predict(new_emails)
print(predictions)  # e.g., [1 0] => spam, not spam
