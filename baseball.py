# -*- encoding: utf-8 -*-

import random


class myGame:
    
    def __init__(self,title):
		self.title=title

    def start(self):
		pass

    def gettitle(self):
		return self.title


class updownGame(myGame):
    
    def __init__(self, title, lower=1,upper=9):
        myGame._init_(self, title)
        self.lower=lower
        self.upper=upper


    def start(self):
        print 'limit:', self.lower,self.upper
		
        rn = random.randint(self.lower,self.upper)

        while True:
		an = input("Input:")

		if an == rn:
			print "Right"
			break
		elif an>rn:
			print "Down"
		else:
				print "Up"

	def setlimit(self,lower,upper):
		self.lower=lower
		self.upper=upper

	def getlimit(self):
		return self.lower, self.upper



class baseballGame(myGame):
    
    def __init__(self,title):
        myGame.__init__= title
    
    
class baseballGame3(baseballGame):
    
    def __init__(self,title):
        baseballGame.__init__= title

    def start(self):
        
        rn1 = random.randint(1,9)
        rn2=rn1
        rn3=rn1
        
        while True:
            if rn1 == rn2:
                rn2 = random.randint(1,9)
            else:
                break
        
        while True:
            if rn1 == rn3 or rn2 == rn3:
                rn3 = random.randint(1,9)
            else:
                break
            
        rnlist= [rn1,rn2,rn3]
        #append는 몇개를 추가할 지 모를 때 사용한다
        
        print rnlist        
        
        while True:
            an = raw_input("input:")
        
            anlist = [int(an[0]),int(an[1]),int(an[2])]
        
            strike = 0
            ball = 0
        
            for i in range(len(rnlist)):
                for j in range(len(anlist)):
                    if rnlist[i] == anlist[j] and i == j:
                        strike = strike + 1
                    if rnlist[i] == anlist[j] and i == j:
                        ball = ball + 1
               
            print 'strike:', strike, 'Ball', ball
            
            if strike == 3:
                break
         
    
class baseballGame4(baseballGame):
    
    def __init__(self):
        pass
    

if __name__=='__main__':
#	myclass = updownGame(upper=100)
#	print myclass.getlimit()
#	myclass.start()
#	myclass.setlimit(10,20)
#	myclass.start()
#     myclass.getTitle()
#     myclass.start()

    myinst = baseballGame3('gg')
    myinst.start()