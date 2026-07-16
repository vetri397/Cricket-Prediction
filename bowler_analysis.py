import pandas as pd

# Load deliveries
deliveries = pd.read_csv("data/deliveries.csv")

batter = input("Enter Batter Name: ")

player_data = deliveries[
    deliveries["batter"] == batter
]

# Group by bowler
stats = player_data.groupby("bowler").agg(
    Runs=("batsman_runs", "sum"),
    Balls=("ball", "count"),
    Outs=("player_dismissed",
          lambda x: x.notna().sum())
)

stats["Strike Rate"] = (
    stats["Runs"] /
    stats["Balls"]
) * 100

stats = stats.sort_values(
    by="Runs",
    ascending=False
)

print("\n========== BOWLER ANALYSIS ==========\n")
print(stats.head(20))