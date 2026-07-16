import pandas as pd

# Load datasets
deliveries = pd.read_csv("data/deliveries.csv")
matches = pd.read_csv("data/matches.csv")

batter = input("Enter Batter Name: ")
team = input("Enter Opponent Team: ")

# Find all matches against the selected team
match_ids = matches[
    (matches["team1"] == team) | (matches["team2"] == team)
]["id"]

# Get batter data from those matches
player_data = deliveries[
    (deliveries["match_id"].isin(match_ids)) &
    (deliveries["batter"] == batter)
]

# Group by bowler
stats = player_data.groupby("bowler").agg(
    Runs=("batsman_runs", "sum"),
    Balls=("ball", "count"),
    Outs=("player_dismissed", lambda x: x.notna().sum())
)

stats["Strike Rate"] = (stats["Runs"] / stats["Balls"]) * 100

stats = stats.sort_values("Runs", ascending=False)

print("\n===== PERFORMANCE AGAINST", team, "=====\n")
print(stats)