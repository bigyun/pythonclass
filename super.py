#!/usr/bin/python
# coding: utf-8
#普通继承

'''
class FooParent(object):
	def bar(self,message):
		print "Parent"+" "+message

class FooChild(FooParent):
	def bar(self,message):
		FooParent.bar(self,message)
'''

#super继承

class FooParent(object):
	def bar(self,message):
		print "Parent"+" "+message

class FooChild(FooParent):
	def bar(self,message):
		super(FooChild,self).bar(message)
if __name__ == '__main__':
	fooChild = FooChild()
	fooChild.bar("helloworld")

