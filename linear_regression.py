import pandas as pd
# Importing the dataset
dataset = pd.read_csv('data/ipl.csv')
X = dataset.iloc[:,[3,4,7,8,9,12,13]].values
y = dataset.iloc[:, 14].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(X_train,y_train)

# Testing the dataset on trained model
y_pred = lin.predict(X_test)
score = lin.score(X_test,y_test)*100
print("R square value:" , score)

# Testing with a custom input
import numpy as np
new_prediction = lin.predict(sc.transform(np.array([[3,6,48,0,6,23,22]])))
print("Prediction score:" , new_prediction)

