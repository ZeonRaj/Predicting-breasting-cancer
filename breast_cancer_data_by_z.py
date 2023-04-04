# -*- coding: utf-8 -*-
"""Breast cancer data by Z.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dm65-vno1nQr5g6HM8YuY1xxiHox2jkz

Sample Breast Cancer Diagnosis. GUVI project
"""

# impor libraries
import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# loading the data from sklearn 
#breast_cancer_data = pd.load_csv("cancer.csv")
#Assigning a variable for the data set 
#lets assign BC_dataset- breast cancer dataset
BC_dataset = sklearn.datasets.load_breast_cancer()

print(BC_dataset)
#show the data in numnpy array

# load the dataframe & print first 5 row
data_frame = pd.DataFrame(BC_dataset.data, columns = BC_dataset.feature_names)
data_frame.head()

#show the rows and columns
data_frame['label'] = BC_dataset.target# adding target table

data_frame.shape

#to show the data heading in columns
data_frame.info()

# statistical measures about the data
data_frame.describe()

# checking the distribution of Target Varibale
# 1 - benign
# 0- malignant
data_frame['label'].value_counts()

data_frame.groupby('label').mean() #find the mean values of the lable data

#spliting the input data
X = data_frame.drop(columns='label', axis=1)
Y = data_frame['label']

print(X)

print(Y)

#spliting test and train data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()

# training the Logistic Regression model using Training data

model.fit(X_train, Y_train)

# the accuracy of data
X_train_prediction =model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy on training data = ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Accuracy on test data = ', test_data_accuracy)

"""***THE RESULT PREDICTION***"""

#the accuracy of train data is 95% and for test data is 93%
# the indput data is taken from the csv file given in below 

#84862001,M,16.13,20.68,108.1,798.8,0.117,0.2022,0.1722,0.1028,0.2164,0.07356,0.5692,1.073,3.854,54.18,0.007026,
#0.02501,0.03188,0.01297,0.01689,0.004142,20.96,31.48,136.8,1315,0.1789,0.4233,0.4784,0.2073,0.3706,0.1142  


sample_input_data = (16.13,20.68,108.1,798.8,0.117,0.2022,0.1722,0.1028,0.2164,0.07356,0.5692,1.073,3.854,54.18,0.007026,0.02501,0.03188,0.01297,0.01689,0.004142,20.96,31.48,136.8,1315,0.1789,0.4233,0.4784,0.2073,0.3706,0.1142)

# convert the tuple to np array
np_converted_data = np.asarray(sample_input_data)

# reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = np_converted_data.reshape(1,-1)

predicted_sample = model.predict(input_data_reshaped)
print(predicted_sample)

if (predicted_sample[0] == 0):
  print('Tumor Type : Malignant')

else:
  print('Tumor Type : Benign')



