# Niave bayes classifier

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report

data=pd.read_csv('../5.csv')
x=data[['feature1','feature2','feature3']]
y=data['target']

xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.3)

nbClassifier=GaussianNB()
nbClassifier.fit(xTrain,yTrain)

predict=nbClassifier.predict(xTest)

print("Accuracy: ",accuracy_score(yTest,predict))
print("Precision: ",precision_score(yTest,predict,average='macro'))
print("Recall: ",recall_score(yTest,predict,average='macro'))
print("Classification report: ",classification_report(yTest,predict))


feature1,feature2,feature3,target
5.1,3.5,1.4,0
4.9,3.0,1.4,0
4.7,3.2,1.3,0
4.6,3.1,1.5,0
5.0,3.6,1.4,0
7.0,3.2,4.7,1
6.4,3.2,4.5,1
6.9,3.1,4.9,1
5.5,2.3,4.0,1
6.5,2.8,4.6,1
7.6,3.0,6.6,2
4.9,2.5,4.5,2
7.3,2.9,6.3,2
6.7,2.5,5.8,2
7.2,3.6,6.1,2


