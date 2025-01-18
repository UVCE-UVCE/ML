# KNN 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=load_iris()
print("Feature Name: ",iris.feature_names)
print("Iris Data: ",iris.data)
print("Target Name: ",iris.target_names)
print("Target : ",iris.target)

xTrain,xTest,yTrain,yTest=train_test_split(iris.data,iris.target,test_size=0.25)

clf=KNeighborsClassifier()
clf.fit(xTrain,yTrain)

print("Accuracy: ",clf.score(xTest,yTest))
prediction=clf.predict(xTest)
print("Prediction: ",prediction)
print("Test Data: ",yTest)
diff=prediction-yTest
print("Result: ",diff)
print("Number of Mismatched Samples = ", abs(sum(diff)))