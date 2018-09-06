import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

learning_rate=0.9
loops=100
class_labels=[]
hidden_nodes=5
#file=input("Enter the file name:")


def sigma(val):
	return 1/(1+np.exp(-val))

def train(setX,setY,testX,testY):
	global learning_rate
	global loops
	global hidden_nodes
	weights_ItoH=[[1/(setX.shape[1]*5) for i in range(hidden_nodes)]for j in range(setX.shape[1])]  
	weights_HtoO=[0.2 for i in range(hidden_nodes)]
	bias1=[1/6 for i in range(hidden_nodes)]
	bias2=1/6
	while loops!=0:
		for i in range(setX.shape[0]):
			curr=np.array(list(setX.iloc[i]))
			curry=setY.iloc[i]

			op1=sigma(np.dot(curr,weights_ItoH)+np.array(bias1))
			op2=sigma(np.dot(op1,weights_HtoO)+np.array(bias2))

			if op2>=0.5:
				pred=1
			else:
				pred=0

			op_error=op2*(1-op2)*(curry-pred)
			hidden_err=np.dot(((op1*op_error)*np.array(1-np.array(op1))),weights_HtoO)

			weights_HtoO=np.array(weights_HtoO)+learning_rate*op2*np.array(op_error)
			weights_ItoH=np.array(weights_ItoH)+np.reshape(learning_rate*np.array(op1)*hidden_err,(-1,hidden_nodes))
			bias1=np.array(bias1)+learning_rate*np.array(hidden_err)
			bias2=np.array(bias2)+learning_rate*np.array(op_error)
		loops=loops-1

	return test(testX,testY,weights_ItoH,weights_HtoO,bias1,bias2)

def test(setX,setY,weights_ItoH,weights_HtoO,bias1,bias2):
	global learning_rate
	global hidden_nodes
	count=0
	tp=0.01
	tn=0.01
	fp=0.01
	fn=0.01
	for i in range(setX.shape[0]):
		curr=np.array(list(setX.iloc[i]))
		curry=setY.iloc[i]

		op1=sigma(np.dot(curr,weights_ItoH)+np.array(bias1))
		op2=sigma(np.dot(op1,weights_HtoO)+np.array(bias2))

		if op2>=0.5:
			pred=1
		else:
			pred=0
		error=curry-pred
		if error==0:
			count=count+1
		if pred==curry and pred==1:
			tp=tp+1
		if pred!=curry and pred==1:
			fp=fp+1
		if pred!=curry and pred==0:
			fn=fn+1
		

	return float(count/setX.shape[0]),float(tp/(tp+fp)),float(tp/(tp+fn))

def main():
	file=input("Enter the file name:")
	data=pd.read_csv(file)
	class_labels = list(set(data['class']))

	for i in range(len(class_labels)):
		data.loc[data['class'] == class_labels[i], 'class'] = i

	X=data.iloc[:,:data.shape[1]-1]
	Y=data.iloc[:,data.shape[1]-1]
	sumacc=0
	sumpre=0
	sumrec=0
	for i in range(10):
		trainX,testX,trainY,testY = train_test_split(X,Y, train_size=0.8,random_state=1000)

		acc,pre,rec,=train(trainX,trainY,testX,testY)
		sumacc+=acc
		sumpre+=pre
		sumrec+=rec
	print("Accuracy=",sumacc/10,"\tPrecision=",sumpre/10,"\tRecall=",sumrec/10)

if __name__ == '__main__':
	main()