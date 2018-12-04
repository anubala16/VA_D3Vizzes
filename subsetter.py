import pandas as pd

file = "data_subset.csv"
df = pd.read_csv(file)

for i in range(500):
    df.loc[[i]].to_csv('first500.csv', 'a')
