import pandas as pd
file = 'market_trend_copy.csv'
df = pd.read_csv(file, sep = ',')
print(df.head())
# print(df.index.columns())
