import pandas as pd
data = pd.read_csv('marketTrendInUTC.csv')

df=data.sort_values(by='Date')

print(df)