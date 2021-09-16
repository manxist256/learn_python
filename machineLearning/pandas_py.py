import pandas as pd

df = pd.read_csv("../inputxyz_avc.csv")
pd.read_orc("../inputxyz_avc.orc")
print(df)
print(df.shape)
print(df.describe())
print(df.values)