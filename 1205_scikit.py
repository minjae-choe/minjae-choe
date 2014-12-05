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
clf.fit(X, y)  
clf.predict(X)

