import pandas as pd
df = pd.read_csv('flights.csv')
df.index=["6E-7542","6E-4885","6E-4589"]
print(df)
