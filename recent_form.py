import pandas as pd

# Load dataset
deliveries = pd.read_csv("data/deliveries.csv")

player = input("Enter Batter Name: ")

# Get only that batter's data
player_data = deliveries[deliveries["batter"] == player]

# Runs scored in each match
match_runs = player_data.groupby("match_id")["batsman_runs"].sum()

# Last 5 matches
last5 = match_runs.tail(5)

print("\n===== LAST 5 MATCHES =====")
print(last5)

print("\nAverage Runs:", round(last5.mean(),2))
print("Highest Score:", last5.max())
print("Lowest Score:", last5.min())