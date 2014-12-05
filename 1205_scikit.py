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

sum0 = 0
sum1 = 0
sum2 = 0

for i, ix in enumerate(y):
    if ix == 0:
        sum0 = sum1 + 1
    elif ix == 1:
        sum1 = sum1 + 1
    else:
        sum2 = sum2 + 1
    
c0 = np.rint(sum0 * 0.6)
c1 = np.rint(sum1 * 0.6)
c2 = np.rint(sum2 * 0.6)    
    
arrx0 = X[:c0]
arry0 = y[:c0]
arrx1 = X[sum0:sum+c1]
arry1 = y[sum0:sum0+c1]
arrx2 = X[sum0+sum1:sum0+sum1+c2]
arry2 = y[sum0+sum1:sum0+sum1+c2]    
    
    
#a = np.array([[1, 2], [3, 4]])
#b = np.array([[5, 6]])
#np.concatenate((a, b), axis=0)

np.concatenate((arrx0, arrx1), axis=0)