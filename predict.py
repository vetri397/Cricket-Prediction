import pandas as pd
import joblib

# Load trained model
model = joblib.load("cricket_predictor.pkl")

# Load features dataset
df = pd.read_csv("features.csv")

player = input("Enter Batter Name: ")

# Get latest record of player
player_data = df[df["batter"] == player]

if player_data.empty:
    print("Player not found!")
else:
    latest = player_data.iloc[-1]

    X = [[
        latest["Career_Avg"],
        latest["Last5_Avg"],
        latest["Strike Rate"],
        latest["Fours"],
        latest["Sixes"]
    ]]

    prediction = model.predict(X)

    print("\n========== AI Prediction ==========")
    print("Player :", player)
    print("Career Average :", round(latest["Career_Avg"],2))
    print("Last 5 Average :", round(latest["Last5_Avg"],2))
    print("Strike Rate :", round(latest["Strike Rate"],2))
    print("Predicted Runs :", round(prediction[0]))