import pandas as pd

features = pd.read_csv("features.csv")

print("Features Shape:")
print(features.shape)

print("\nFeatures Columns:")
print(features.columns.tolist())

print("\nFirst 5 Rows:")
print(features.head())