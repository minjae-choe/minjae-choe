# -*- coding: utf-8 -*-

import random




    def setLimit(self, lower, upper)
        self.lower = lower
        self.upper = upper

    def getLimit(self):
        return self.lower, self.upper


class baseballGame(myGame):
    
    def _init_(self, title):
        myGame._init_= title
    
    
class baseballGame3(baseballGame):
    
    def _init_(self, title):
        baseballGame._init_=title
        
    def start(self):
        
        rn1 = random.randint(1,9)
        rn2 = rn1
        rn3 = rn1

        while True:
            if rn1 == rn2:
                rn2 = random.randint(1,9)
            else:
                break
            
        while True:
            if rn1 == rn3 or rn2 ==rn3:
                rn3 = random.randint(1,9)
            else:
                break
        
class baseballGame4(baseballGame):