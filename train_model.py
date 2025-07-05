# Author: Syed Mohammad Askari Abidi

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv("dataset.csv")

# Drop timestamp (not needed for ML)
df.drop("timestamp", axis=1, inplace=True)

# Encode label
df['label'] = df['label'].map({'normal': 0, 'anomaly': 1})

# Features & target
X = df.drop("label", axis=1)
y = df["label"]

# scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler
joblib.dump(scaler, "scaler.pkl")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Try multiple models
models = {
    "RandomForest": RandomForestClassifier(),
    "SVM": SVC(),
    "IsolationForest": IsolationForest(contamination=0.1)
}

for name, model in models.items():
    print(f"\n🔍 Training {name}...")
    if name == "IsolationForest":
        model.fit(X_train)
        y_pred = model.predict(X_test)
        y_pred = [0 if p == 1 else 1 for p in y_pred]  # Adjust label (1 = anomaly)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    print(f"\n📊 Results for {name}:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Save best model
best_model = RandomForestClassifier()
best_model.fit(X_scaled, y)
joblib.dump(best_model, "model.pkl")

print("\n✅ Model and scaler saved!")
