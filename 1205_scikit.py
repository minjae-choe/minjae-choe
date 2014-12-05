# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 10:49:30 2014

@author: user
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print iris

print digits

from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
s = np.rint(iris.data.shape[0]*0.6)
clf.fit(X[:s], y[:s])  
clf.predict(X[s:])

for i, ix in enumerate(y):
    if ix == 0:
        pass
    elif ix == 1:
        pass
    else:
        pass
    
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
