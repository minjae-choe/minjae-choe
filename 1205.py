# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 09:14:14 2014

@author: user
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

lst=[4,-7,5,3]


print lst

obj=Series([4,-7,5,3])

#인덱스는 자동으로 0부터 순서대로 들어감

print obj

print obj.values

print obj.index

obj2=Series(lst,index=['d','b','a','c'])


print obj2

obj22=Series(lst,index=[2010,2011,2012,2013])

print obj22

print obj2['a']


obj2['d']=6

print obj2[['a','c','d']]

obj222 = (obj2[obj2>0])

print obj222

print ('b' in obj2)

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}

obj3=Series(sdata)

print obj3

states = ['Califonia','Ohio','Oregon','Texas']

obj4=Series(sdata,index=states)

print obj4

print pd.isnull(obj4)

print pd.notnull(obj4)


print obj3+obj4

obj4.name = 'Population'

obj4.index.name = 'State'

print obj4

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada'],
        'year': [2000,2001,2002,2001,2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
        
frame = DataFrame(data)

print frame

frame = DataFrame(data, columns=['year', 'state', 'pop'])

print frame

frame2 = DataFrame(data,
        columns=['year', 'state', 'pop', 'debt'],
        index=['one', 'two', 'three', 'four', 'five'])

print frame2

print frame2['state']

print frame2.year

print frame2.ix['three']

frame2['debt'] = 16.5

print frame2

frame2['debt'] = np.arange(5.)

print frame2

val = Series([-1.2, -1.5, -1,7],
             index=['two', 'four', 'five'])
             
frame2['debt'] = val

print frame2

frame2['eastern'] = (frame2.state == 'Ohio')

print frame2

del frame2['eastern']

print frame2

print frame2.T

obj6 = Series(range(3),
              index=['a','b','c'])
index = obj6.index
print index
print index[1:]
#index[1] = 'd'

index = pd.Index(np.arange(3))

obj7 = Series([1.5, -2.5, 0.],
              index=index)
              
print obj7
print obj7.index is index

obj = Series([4.5, 7.2, -5.3, 3.6],
             index=['d','b','a','c'])
             
print obj

obj2 = obj.reindex(['a','b','c','d','e'])

print obj2

obj3 = oibj.reindex(['a','b','c','d','e'],
                    fill_value=0)

print obj3

obj4 = Series(['blue', 'purple', 'yellow'],
              index=[0,2,4])
              
obj5 = obj4.reindex([range(6),
                    method='ffill')
                    
print obj5

obj6 = obj4.reindex([range(6)],
                    method='bfill')
                    
print obj6

obj = Series(np.arange(5.),
             index=['a','b','c','d','e])
             
new_obj = obj.drop('c')

print new_obj



                                                 