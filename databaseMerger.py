import pandas as pd

# Main database
dataset = pd.read_csv(
    "data/train.csv", index_col="date", parse_dates=["date"]
).drop(columns=["id"])

# Oil database
dataset2 = pd.read_csv(
    "data/oil.csv", index_col="date", parse_dates=["date"]
)

dataset = dataset.merge(dataset2, how="left", on="date")

# Holiday database, but only the type (might need to change that??)
dataset3 = pd.read_csv(
    "data/holidays_events.csv", index_col="date", parse_dates=["date"]
)[["type"]]

dataset = dataset.merge(dataset3, how="left", on="date")

# Stores database, once again only type and cluster, might need more
dataset4 = pd.read_csv(
    "data/stores.csv", index_col="store_nbr"
)[["type", "cluster"]]

dataset = dataset.merge(dataset4, how="left", on="store_nbr")

dataset.to_csv("data/final.csv")