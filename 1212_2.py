# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 09:15:44 2014

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()

#ax = fig.add_subplot(1,1,1)
##피규어라는 공간 크게 하나 들어가있음
#ax1 = fig.add_subplot(2,2,1)
##피규어가 2행 2열에 하나
#ax2 = fig.add_subplot(2,2,2)
#ax3 = fig.add_subplot(2,2,3)
#ax4 = fig.add_subplot(2,2,4)

#plt.plot(np.random.randn(50).cumsum(),'co--')
## 제일 마지막 서브플롯에 자동으로 추가됨
## c는 색깔,o는 포인트에 점 --는 점선, -는 실선
#
#_ = ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
##각 피규어 이름에 바로 접근가능, bins는 전체 구간을 몇개로 나눌 것이냐는 의미, 컬러의 k는 블랙, 알파는 투명도
#ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
##scatter은 산포도, 각각 x값과 y값을 준 것

#fig, axes = plt.subplots(2,2)
##2행 2열, 서브플롯을 한꺼번에 집어넣을 수도 있다
#
#print axes
#
#fig, axes = plt.subplots(2,2, sharex=True)
## x축을 공유
#print axes
## y축을 공유
#fig, axes = plt.subplots(2,2, sharey=True)
#
#print axes
#
#fig, axes = plt.subplots(2,2, sharex=True,sharey=True)
#
#for i in range(2):
#    for j in range(2):
#        axes[i,j].hist(np.random.randn(500),bins=50, color='k')
#plt.subplots_adjust(wspace=0, hspace=0)
##wspace와 hspace는 플롯 크기에 비례하게 피규어사이 공간을 띄워라, 위는 0이라서 피규어들 붙어있음
#
#data=np.random.randn(30).cumsum()
#
#plt.plot(data,'k--', label='Default')
##점선형태, 일반적인 선
#plt.plot(data, 'k-', drawstyle='steps-post',lavel='steps-post')
##실선형태, 직선형태
#plt.legend(loc='best')
##그래프 이름 표시하기, best는 그래프랑 안 걸리는 최적의 위치 찾기

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#ax.plot(np.random.randn(1000).cumsum())
##cumsum은 랜덤시켜 발생한 값을 앞에값들과 계속 더한값을 그래프에 찍는다
#tick = ax.set_xticks([0,250,500,750,1000])
##표에 표시되는 간격을 직접 정해줄 수 있다
#labels = ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
##그러한 표시되는 간격의 형태를 지정가능, rotation은 휘어지게)
#
#ax.set_title('My Plot')
##전체 플롯에 이름 부과
#ax.set_xlabel('Stages')
##x축에 이름
#ax.set_ylabel('values')
#
#
#a = np.arange(10)
#
#print a
#
#print a.cumsum()
#
#
#
#
#from datetime import datetime
#
#fig=plt.figure()
#ax= fig.add_subplot(1,1,1)
#
#data=pd.read_csv('spx.csv',index_col=0,parse_dates=True)
##파일을 불러들이는법, index_col은 0번째 행에 있다, 파이썬내에서 이해할 수 있는 숫자로 바꾸라는 true
#spx = data['SPX']
#
#spx.plot(ax=ax, style='k--')
#
#crisis_data = [
#    (datetime(2007,10,11), 'Peak of bull market'),
#    (datetime(2008,3,12), 'Bear Stearns Fails'),
#    (datetime(2008,9,15), 'Lehman Bankruptcy')
#]
##crisis_data는 항목이 2개씩 있는 튜플형태의 리스트 형태이므로, for datam label in crisis_data로 받을 수 있다
#
#for date, label in crisis_data:
#    ax.annotate(label,
#    #annotate는 주석을 다는것
#                xy=(date, spx.asof(date)+50),
#                xytext=(date, spx.asof(date)+200),
#                arrowprops=dict(facecolor='black'),
#                #검정석 화살 추가하라
#                horizontalalignment='left',
#                verticalalignment='top')
#                #좌측정렬 위에 붙여라
# 
#                
#ax.set_xlim(['1/1/2007','1/1/2011'])
#ax.set_ylim([600,1800])
##xlim ylim은 데이터의 범위 정해주는것, 작게 줄수록 그래프 확대되는 것 볼 수 있다
#
#ax.set_title('Important dates in 2008-2009 financial crisis')
#
#fig=plt.figure()
#
#ax = fig.add_subplot(1,1,1)
#
#rect=plt.Rectangle((0.2,0.75),
#                   0.4,
#                   0.15,
#                   color='k',
#                   alpha=0.3)
#                   
#circ=plt.Circle((0.7,0.2),
#                0.15,
#                color='r',
#                alpha=0.5)
#                
#pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],
#                 color='g',
#                 alpha=0.5)
#                 
#ax.add_patch(rect)
#ax.add_patch(circ)
#ax.add_patch(pgon)
#
#plt.savefig('shape.svg', dpi=600)
##해당 그래프가 바로 저장이됨, dpi는 해상도(dot per inch))

#s = pd.Series(np.random.randn(10).cumsum(),
#             index=np.arange(0,100,10))#0부터 99까지 증가하는데, 10씩 증가하라
#s.plot()
##판다스로 그래프 그리기
#
#df=pd.DataFrame(np.random.randn(10,4).cumsum(0),
#                #10행 4열짜리 random array만든 것 
#                columns=['A','B','C','D'],
#                index=np.arange(0,100,10))
#
##df.plot(logy=True)
###y축이 로그형으로 변환되어 나타남
#
#df.plot(xlim=50,title='My')
##앞서와 같이 범위 지정가능, 위는 x는 50부터 시작

#fig, axes = plt.subplots(2,1)
#
#data=pd.Series(np.random.randn(16),
#               index=list('abcdefghijklmnop'))
#
#data.plot(kind='bar',ax=axes[0])
##수직형태의 막대그래프 그리기
#data.plot(kind='barh',ax=axes[1])
##가로방향의 막대그래프 그리기

#df=pd.DataFrame(np.random.randn(6,4),
#                index=['one','two','three','four','five','six'],
#                columns=pd.Index(['A','B','C','D'], name='Genus'))
#                
#df.plot(kind='bar')
#
#df.plot(kind='barh',stacked=True)
##stacked는 누적형태로

#tips=pd.read_csv('tips.csv')
#tips['tip_pct']=tips['tip']/tips['total_bill']
#tips['tip_pct'].hist(bins=50)
#tips['tip_pct'].plot(kind='kde')

#comp1 = np.random.normal(0,1,size=200)
#comp2 = np.random.normal(10,2,size=200)
##평균,표준편차 순으로 전달받는 정규분포그래프
#values=pd.Series(np.concatenate((comp1, comp2)))
#
#values.hist(bins=100, normed=True)
#values.plot(kind='kde')

macro = pd.read_csv('macrodata.csv')

data=macro[['cpi','m1','tbilrate','unemp']]

trans_data = np.log(data).diff().dropna()
#데이터 값 차이 너무 크면 그래프 퍼지기 때문에 로그 시킴, diff는 로그시킨 값들의 차이를 반환하라는 뜻이고, dropna는 none값을 날리라는 뜻(첫 번째는 차이비교 불가능하므로)
plt.scatter(trans_data['m1'], trans_data['unemp'])

pd.scatter_matrix(trans_data, diagonal='kde')
#산포도 그래프