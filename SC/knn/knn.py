from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import random
import heapq


class heapobj:
	def __init__(self):
		self.eq_dist
		self.y_val

	def __lt__(self,other):
    	return self.eq_dist < other.eq_dist
data=input("enter the name of the dataset file:")

df=pd.read_csv(data)

number=LabelEncoder()
df['class']=number.fit_transform(df['class'].astype('str'))


X=df.iloc[:,:df.shape[1]-1]

Y=df.iloc[:,df.shape[1]-1]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
k=11


def predict(X_train,X_test,Y_train,Y_test):
	for i in range(X_test.shape[0]):
		L=[]
		test_row=list(X_test.iloc[i])
		curr_y=Y_test.iloc[i]
		for j in range(X_train.shape[0])
		