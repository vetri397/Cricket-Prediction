import pandas as pd

# Load data
deliveries = pd.read_csv("data/deliveries.csv")

player = input("Enter Batter Name: ")

player_data = deliveries[deliveries["batter"] == player]

runs = player_data["batsman_runs"].sum()
balls = len(player_data)
innings = player_data["match_id"].nunique()

fours = (player_data["batsman_runs"] == 4).sum()
sixes = (player_data["batsman_runs"] == 6).sum()

outs = (player_data["player_dismissed"] == player).sum()

average = runs / outs if outs > 0 else runs
strike_rate = (runs / balls) * 100 if balls > 0 else 0

print("\n========== PLAYER CAREER ==========")
print("Player :", player)
print("Matches :", innings)
print("Runs :", runs)
print("Balls :", balls)
print("Outs :", outs)
print("Average :", round(average,2))
print("Strike Rate :", round(strike_rate,2))
print("Fours :", fours)
print("Sixes :", sixes)