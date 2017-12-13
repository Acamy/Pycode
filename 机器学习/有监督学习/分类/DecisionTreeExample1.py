from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

clf  = DecisionTreeClassifier()

iris = load_iris()

print(cross_val_score(clf,iris.data,iris.target,cv=10))


X = [[0],[1],[2],[3]]
y = [0,0,1,1]

clf.fit(X,y)
print(clf.predict([[1.5],[1.6]]))