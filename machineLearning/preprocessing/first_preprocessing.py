import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read sales_data
sales_data = pd.read_csv("../ml/P1/Part1/Python/Data.csv")

# read all rows (and) read first 3 columns
X = sales_data.iloc[:, :-1] #still pandas df
# read all rows (and) read only last column
Y = sales_data.iloc[:, -1] #still pandas df

X = X.values #numpy df
Y = Y.values #numpy df

from sklearn.impute import SimpleImputer
#fill missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3]) #will look for all the missing values in all rows (and) columns 1 [Age] and 2 [Salary]
#Always include all the measure columns for filling the missing values
X[:, 1:3] = imputer.transform(X[:, 1:3])

#encode categorical values for X
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# 0th index is the only Categorical column here in X
ct = ColumnTransformer(transformers=[('encoding', OneHotEncoder(), [0])], remainder='passthrough')
r = ct.fit_transform(X)
X = np.array(r)
#print(X)

#encode categorical values for Y
from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
Y = lc.fit_transform(Y)
#print(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
print(X_train)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.fit_transform(X_test[:, 3:])
print(X_train)


