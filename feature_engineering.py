import pandas as pd

# Load player-match dataset
df = pd.read_csv("player_match_stats.csv")

# Sort by batter and match
df = df.sort_values(["batter", "match_id"])

# Career average before current match
df["Career_Avg"] = (
    df.groupby("batter")["Runs"]
      .expanding()
      .mean()
      .shift(1)
      .reset_index(level=0, drop=True)
)

# Last 5 matches average before current match
df["Last5_Avg"] = (
    df.groupby("batter")["Runs"]
      .rolling(5)
      .mean()
      .shift(1)
      .reset_index(level=0, drop=True)
)

# Fill missing values
df["Career_Avg"] = df["Career_Avg"].fillna(0)
df["Last5_Avg"] = df["Last5_Avg"].fillna(0)

print(df.head(15))

# Save
df.to_csv("features.csv", index=False)

print("\n✅ features.csv created successfully!")