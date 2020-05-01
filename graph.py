import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px
# import csv

file = 'market_trend_copy.csv'
df = pd.read_csv(file)
# df[["Date", 'Index', "Previous close"]]
df = df.columns.tolist()
# print(df)
try:
    df.plot(kind = 'line', x = 'Index', y = 'Previous close')    
    print(df)
    df.show()
except Exception as exp:
    print("Error")