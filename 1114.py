# -*- coding: utf-8 -*-

import random

class myGame:
	def _init_(self):
		pass

	def start():
		pass
	def _init_(self):
		pass

class updownGame(myGame):
	def _init_(self):
		pass

	def start(self):
		rn = random.randint(1,9)

		while True:
			an = input("Input:")

			if an == rn:
				print "Right"
			elif an > rn:
				print "Down"
			else:
				print "Up"

class baseballGame(myGame):
	def _init_(self):
		pass

class baseballGame3(baseballGame):
	def _init_(self):
		pass

if __name__ == '__main__':
	myclass = updownGame()
	myclass.start()
