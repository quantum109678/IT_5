from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import random

data=input("enter the name of the dataset file:")

df=pd.read_csv(data)

number=LabelEncoder()
df['class']=number.fit_transform(df['class'].astype('str'))


X=df.iloc[:,:df.shape[1]-1]

Y=df.iloc[:,df.shape[1]-1]



def sigmoid(val):
	return 1/(1+np.exp(-val))

def train(X_train,Y_train,hu):
	weights2=[0.2 for i in range(hu)]
	weights=[[1/(X_train.shape[1]*5) for j in range(hu)] for i in range(X_train.shape[1])]
	bias1=[1/6 for i in range(hu)]
	bias2=1/6
	loop,rate=10,0.9
	while(loop!=0):
		for i in range(X_train.shape[0]):
			cr=np.array(list(X_train.iloc[i]))
			y=Y_train.iloc[i]
			#feedforward
			output1=sigmoid(np.dot(cr,weights)+np.array(bias1))
			output2=sigmoid(np.dot(output1,weights2)+np.array(bias2))
			if(output2>=0.5):
				prediction=1
			else:
				prediction=0
			#backprop
			output_error=output2*(1-output2)*(y-prediction)
			hidden_error=np.dot(((output1*output_error)*np.array(1-np.array(output1))),weights2)
			#modifying weights and biases
			weights2=np.array(weights2)+rate*output2*np.array(output_error)
			weights=np.array(weights)+np.reshape(rate*np.array(output1)*hidden_error,(-1,hu))
			bias1=np.array(bias1)+rate*np.array(hidden_error)
			bias2=np.array(bias2)+rate*np.array(output_error)
		loop=loop-1
	#
	return weights,weights2,bias1,bias2

def testing(X_test,Y_test,w1,w2,b1,b2):
	count=0
	truep=0.01
	falsep=0.01
	falsen=0.01
	truen=0.01
	#print("Testing:")
	for i in range(X_test.shape[0]):
		cr=list(X_test.iloc[i])
		y=Y_test.iloc[i]
		prediction=-1
		#feedforward
		output1=sigmoid(np.dot(cr,w1)+np.array(b1))
		output2=sigmoid(np.dot(output1,w2)+np.array(b2))
		if(output2>=0.5):
			prediction=1
		else:
			prediction=0
		#string="Expected:"+str(prediction)+" Actual:"+str(y)
		if(prediction==y and prediction==1):
			truep+=1
		if(prediction!=y and prediction==1):
			falsep+=1
		if(prediction!=y and prediction==0):
			falsen+=1
		if(prediction==y and prediction==0):
			truen+=1
		#print(string)
		error=y-prediction
		if(error==0):
			count+=1

	print(float(count/X_test.shape[0]))
	#print(" ")

	return float(count/X_test.shape[0]),float(truep/(truep+falsep)),float(truen/(truen+falsen)),float(truep/(truep+falsen)),float(truen/(truen+falsep))

sumacc=0
sumprep=0
sumpren=0
sumrecp=0
sumrecn=0
for i in range(10):
	X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
	w1,w2,b1,b2=train(X_train,Y_train,5)
	acc,prep,pren,recp,recn=testing(X_test,Y_test,w1,w2,b1,b2)
	sumacc+=acc
	sumprep+=prep
	sumpren+=pren
	sumrecp+=recp
	sumrecn+=recn

print("Accuracy is:{}".format(sumacc/10))
print("Precison is:(+)",sumprep/10,"(-)",sumpren/10)
print("Recall is:(+)",sumrecp/10,"(-)",sumrecn/10)



