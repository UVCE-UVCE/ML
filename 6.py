#  Bayesian Network
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

x,y=make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    n_classes=2,
)
xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.25)

clf=GaussianNB()
clf.fit(xTest,yTest)
print("Accuracy: ",clf.score(xTest,yTest))
prediction=clf.predict(xTest)
print("Prediction: ",prediction)
print("Classification Report: ",classification_report(yTest,prediction))

print('For Age enter: 0=SuperSeniorCitizen, 1=SeniorCitizen, 2=MiddleAged, 3=Youth, 4=Teen')
print('For Gender enter: 0=Male, 1=Female')
print('For Family History enter: 0=No, 1=Yes')
print('For Diet enter: 0=High, 1=Medium')
print('For Lifestyle enter: 0=Athlete, 1=Active, 2=Moderate, 3=Sedentary')
print('For Cholesterol enter: 0=High, 1=BorderLine, 2=Normal')


age = int(input('Enter Age (0=SuperSeniorCitizen, 1=SeniorCitizen, 2=MiddleAged, 3=Youth, 4=Teen): '))
gender = int(input('Enter Gender (0=Male, 1=Female): '))
family_history = int(input('Enter Family History (0=No, 1=Yes): '))
diet = int(input('Enter Diet (0=High, 1=Medium): '))
lifestyle = int(input('Enter Lifestyle (0=Athlete, 1=Active, 2=Moderate, 3=Sedentary): '))
cholesterol = int(input('Enter Cholesterol (0=High, 1=BorderLine, 2=Normal): '))

user_input=np.array([[age,gender,family_history,diet,lifestyle,cholesterol]])
ans=clf.predict(user_input)

if ans==1:
    print("YES")
else:
    pritn("NO")