import pandas as pd

dataset1 = pd.read_csv("merged.csv")
dataset1 = dataset1[dataset1["proper_name"].notna()]
dataset1 = dataset1[dataset1["distance"].notna()]
dataset1 = dataset1[dataset1["mass"].notna()]
dataset1 = dataset1[dataset1["radius"].notna()]

dataset1.to_csv("final.csv", index=False)