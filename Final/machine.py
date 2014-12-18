# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 19:59:43 2014

@author: user
"""


data=pd.read_csv('data.csv',index_col=0,parse_dates=True)


from sklearn import svm
from sklearn import datasets
import numpy as np

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target

result = clf.predict(X[stan_slice:])
print result
