import pandas as pd

# Load deliveries dataset
deliveries = pd.read_csv("data/deliveries.csv")

# Group by Match and Batter
player_match = deliveries.groupby(["match_id", "batter"]).agg(
    Runs=("batsman_runs", "sum"),
    Balls=("ball", "count"),
    Fours=("batsman_runs", lambda x: (x == 4).sum()),
    Sixes=("batsman_runs", lambda x: (x == 6).sum()),
    Outs=("player_dismissed", lambda x: x.notna().sum())
).reset_index()

# Calculate Strike Rate
player_match["Strike Rate"] = (
    player_match["Runs"] / player_match["Balls"]
) * 100

# Save the dataset
player_match.to_csv("player_match_stats.csv", index=False)

print("✅ Dataset Created Successfully!")
print(player_match.head())