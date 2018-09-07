import pandas as pd
import random
from sklearn.model_selection import train_test_split
import numpy as np


class Perceptron:
	def __init__(self, file, learning_rate=0.2):
		self.weights = []
		self.class_labels = []
		self.learning_rate = learning_rate
		self.file = file
		self.MAX_ITER = 100

	def read_dataset(self):
		data = pd.read_csv(self.file)

		self.class_labels = list(set(data['class']))

		for i in range(len(self.class_labels)):
			data.loc[data['class'] == self.class_labels[i], 'class'] = i

		X=data.iloc[:,:data.shape[1]-1]
		Y=data.iloc[:,data.shape[1]-1]

		training_setX,testing_setX,training_setY,testing_setY = train_test_split(X,Y, train_size=0.8)
		self.train(training_setX,training_setY)
		self.test(testing_setX,testing_setY)


	def train(self,tX,tY):
		self.weights=[1/(tX.shape[1]+1) for i in range(tX.shape[1])]
		while self.MAX_ITER!=0:
			for i in range(tX.shape[0]):
				cost=0
				curr=list(tX.iloc[i])
				curry=tY.iloc[i]
				cost=np.dot(self.weights,curr)
				if cost>0:
					cost=1
				else:
					cost=0
				error=curry-cost
				if error!=0:
					for j in range(len(self.weights)):
						self.weights[j]+=self.learning_rate*error*curr[j]
			self.MAX_ITER=self.MAX_ITER-1

		
	
	def test(self,sX,sY):
		tot=sX.shape[0]
		count=0
		truep=0
		truen=0
		falsep=0
		falsen=0
		for i in range(sX.shape[0]):
			curr=list(sX.iloc[i])
			curry=sY.iloc[i]
			cost=np.dot(curr,self.weights)
			if cost>0:
				cost=1
			else:
				cost=0
			#print("Predicted:",str(self.class_labels[cost]),"Actual:",str(self.class_labels[curry]))
			error=curry-cost
			if error==0:
				count=count+1
			if(cost==curry and cost==1):
				truep+=1
			if(cost!=curry and cost==1):
				falsep+=1
			if(cost!=curry and cost==0):
				falsen+=1
			if(cost==curry and cost==0):
				truen+=1
		#print(string)

		print("Accuracy=",float(count/tot))
		print("Precision:",float(truep/(truep+falsep)))
		print("Recall:",float(truep/(truep+falsen)))

def main():
	name=input("Enter the file name:")
	single_perceptron = Perceptron(name)
	single_perceptron.read_dataset()
	

if __name__ == '__main__':
	main()