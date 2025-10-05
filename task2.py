import pandas as pd
import json
import os
import csv

df = pd.read_csv("data.csv")
print("Original Data:")
print(df)

df.to_json("data.json", orient="records", indent=4)
print("\nData has been written to data.json")

with open("data.json", "r") as f:
    data = json.load(f)

filtered_data = [row for row in data if row["age"] > 21]

with open("filtered_data.json", "w") as f:
    json.dump(filtered_data, f, indent=4)

print("\nFiltered data saved to filtered_data.json")
