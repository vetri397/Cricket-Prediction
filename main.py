import pandas as pd

# Load dataset
deliveries = pd.read_csv("data/deliveries.csv")

# User input
batter = input("Enter Batter Name: ")
bowler = input("Enter Bowler Name: ")

# Filter data
matchup = deliveries[
    (deliveries["batter"] == batter) &
    (deliveries["bowler"] == bowler)
]

# Statistics
runs = matchup["batsman_runs"].sum()
balls = len(matchup)
fours = (matchup["batsman_runs"] == 4).sum()
sixes = (matchup["batsman_runs"] == 6).sum()

# Count only dismissals of this batter
dismissals = (matchup["player_dismissed"] == batter).sum()

strike_rate = (runs / balls) * 100 if balls > 0 else 0

print("\n========== BATTER vs BOWLER ==========")
print(f"Batter: {batter}")
print(f"Bowler: {bowler}")
print(f"Runs: {runs}")
print(f"Balls: {balls}")
print(f"4s: {fours}")
print(f"6s: {sixes}")
print(f"Dismissals: {dismissals}")
print(f"Strike Rate: {strike_rate:.2f}")