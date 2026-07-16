import pandas as pd

deliveries = pd.read_csv("data/deliveries.csv")

# Batter vs Bowler Statistics
bowler_stats = deliveries.groupby(["batter","bowler"]).agg(
    Runs=("batsman_runs","sum"),
    Balls=("ball","count"),
    Outs=("player_dismissed",lambda x:x.notna().sum())
).reset_index()

bowler_stats["StrikeRate"] = (
    bowler_stats["Runs"] /
    bowler_stats["Balls"]
) * 100

bowler_stats.to_csv("batter_vs_bowler.csv",index=False)

print("✅ batter_vs_bowler.csv Created")