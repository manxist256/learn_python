import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sales_data = pd.read_csv("../ml/P1/Part1/Python/Data.csv")

X = sales_data.iloc[:, :-1]
Y = sales_data.iloc[:, -1]
print(X)
print(Y)


