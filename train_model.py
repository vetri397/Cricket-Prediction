import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train_model():

    # Load features
    df = pd.read_csv("features.csv")

    # Remove players without enough history
    df = df[df["Last5_Avg"] > 0]

    # Features
    X = df[
        [
            "Career_Avg",
            "Last5_Avg",
            "Strike Rate",
            "Fours",
            "Sixes"
        ]
    ]

    # Target
    y = df["Runs"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    print("Mean Absolute Error:", round(mae, 2))

    joblib.dump(model, "cricket_predictor.pkl")

    print("✅ Model Saved Successfully")

    return model


if __name__ == "__main__":
    train_model()