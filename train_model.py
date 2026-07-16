import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load features
df = pd.read_csv("features.csv")

# Remove rows where Last5_Avg is 0 (not enough history)
df = df[df["Last5_Avg"] > 0]

# Features (Input)
X = df[["Career_Avg", "Last5_Avg", "Strike Rate", "Fours", "Sixes"]]

# Target (Output)
y = df["Runs"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(mae, 2))

# Save model
joblib.dump(model, "cricket_predictor.pkl")

print("\n✅ Model Trained Successfully!")