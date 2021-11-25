import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read sales_data
sales_data = pd.read_csv("../ml/P2/LinearRegression/Python/Salary_Data.csv")

# read all rows (and) read first 3 columns
X = sales_data.iloc[:, :-1]  # still pandas df #YOE #Independent
# read all rows (and) read only last column
Y = sales_data.iloc[:, -1]  # still pandas df #Salary #Dependent

X = X.values  # numpy df
Y = Y.values  # numpy df

# There is no missing files in the file, so ignoring the Imputer logic
# There is no categorical columns here, so ignoring the OneHot encoding here or similar here

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_prediction = lr.predict(X_test)
print(Y_test)
print(Y_prediction)

# Graphs
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, lr.predict(X_train), color='green')
plt.title('Salary vs Experience')
plt.xlabel('YOE')
plt.ylabel('Salary')
plt.show()
