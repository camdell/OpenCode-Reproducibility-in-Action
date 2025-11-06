import numpy as np
import pandas as pd

from numpy.random import default_rng

rng = default_rng(0)

N = 100

method = rng.choice(["A", "B"], size=N)

# Hours spent (self paced), method B participants tend to complete slightly more hours
hours = np.where(
    method == "A",
    rng.normal(loc=10, scale=2, size=N),
    rng.normal(loc=12, scale=2, size=N)
)

score = (
    50
    + np.where(method == "B", 5, 0)           # Method B overall higher
    + 1.5 * hours                             # baseline hours effect
    + np.where(method == "B", 1.5 * hours, 0) # interaction: stronger slope for B
    + rng.normal(0, 5, N)                     # noise
)

df = pd.DataFrame({
    "participant_id": range(1, N + 1),
    "method": method,
    "hours": hours.round(1),
    "score": score.round(1).clip(0, 100)
}).astype({"hours": "object"})

# Introduce realistic irregularities
df.loc[3, "hours"] = None          # missing reported hours
df.loc[7, "score"] = None          # missing test score
df.loc[20, "hours"] = "15"         # incorrect data type
df.loc[50, "score"] = 200          # suspiciously high score
df["0"] = ""                       # irrelevant column from survey system

df.to_csv("raw_training_study.csv", index=False)
print(df.head())
