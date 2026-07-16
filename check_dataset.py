import pandas as pd

# Load datasets
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print("========== MATCHES DATASET ==========")

print("\nMatches Shape:")
print(matches.shape)

print("\nMatches Columns:")
print(matches.columns.tolist())

print("\nMissing Values:")
print(matches.isnull().sum())


print("\n\n========== DELIVERIES DATASET ==========")

print("\nDeliveries Shape:")
print(deliveries.shape)

print("\nDeliveries Columns:")
print(deliveries.columns.tolist())

print("\nMissing Values:")
print(deliveries.isnull().sum())


print("\n\n========== SAMPLE DATA ==========")

print("\nMatches First 5 Rows:")
print(matches.head())

print("\nDeliveries First 5 Rows:")
print(deliveries.head())