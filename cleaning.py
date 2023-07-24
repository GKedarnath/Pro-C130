import pandas as pd
import csv

df = pd.read_csv("final.csv", encoding = "utf-8")
print(df)

df.columns
