# -*- coding: utf-8 -*-
"""lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pq8Ppz_o87CfjU7vRwpynz8roFyJJ7x9
"""

import requests
url = "https://www.dropbox.com/s/veak3ugc4wj9luz/Alumni%20Giving%20Regression%20%28Edited%29.csv"
response = requests.get(url)

with open("Alumni Giving regression (Edited).csv", "wb") as file:
  file.write(response.content)

from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pandas as pd
import csv

import matplotlib.pyplot as plt

from google.colab import files
u = files.upload()

np.random.seed(7)
df = pd.read_csv("Alumni Giving Regression (Edited).csv", delimiter=',')
dd_df_1 = df.head()

print(dd_df_1)

summary_statistics = dd_df_1.describe()
print(summary_statistics)

corr = df.corr(method='pearson')
corr
print(corr)

Y_POSITION = 5
model_1_features = [i for i in range(0,Y_POSITION)]
X = df.iloc[:,model_1_features]
Y = df.iloc[:,Y_POSITION]
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.20,random_state=2020)

model1 = linear_model.LinearRegression()
model1.fit(X_train,y_train)
y_pred_train1 = model1.predict(X_train)
print("Regression")
print("=============================")
RMSE_train1 = mean_squared_error(y_train,y_pred_train1)
print("Regression Train set: RMSE {}".format(RMSE_train1))
print("==========================")
y_pred1 = model1.predict(X_test)
RMSE_test1 = mean_squared_error(y_test,y_pred1)
print("Regression Test set: RMSE {}".format(RMSE_test1))
print("==================")
coef_dict = {}
for coef, feat in zip(model1.coef_,model_1_features):
  coef_dict[df.columns[feat]] = coef
print(coef_dict)

x_values = np.arange(len(y_test))
plt.scatter(x_values,y_test,color='red',label='Predicted')
plt.xlabel('Index or Sequence of Values')
plt.ylabel('Values')
plt.title('Actual vs Predicted Values')
plt.legend()
plt.show()