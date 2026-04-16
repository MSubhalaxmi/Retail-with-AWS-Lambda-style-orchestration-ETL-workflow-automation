import pandas as pd

def enrich_data(file):
    df = pd.read_csv(file)
    df["revenue"] = df["price"] * df["quantity"]
    return df