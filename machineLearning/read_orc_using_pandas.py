import pandas as pd

filename = "/Users/manikandan.kk/hello_world_orc/hxr.orc"

df = pd.read_orc(filename)
print(type(df))
print(df)
