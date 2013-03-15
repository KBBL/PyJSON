from PyJSON import *

if __name__ == "__main__":
	@json_serializable(["field1"])
	class AnotherClass:
		def __init__(self):
			self.field1 = "field"
			self.field2 = "field2"
			#self.field1 = self
	
	@json_serializable(["greeting", "object", "anotherClass", "aList"])
	class Greeting:
		def __init__(self):
			self.greeting = u"Hello"
			self.object = "World"
			self.trans = "Transient"
			self.anotherClass = AnotherClass()
			self.aList = ["Hi", 4.454, 24, AnotherClass(), datetime.date(2013, 1, 3), datetime.time(3,2)]

		def method(self, p1):
			print("This is from 'method({0})'".format(p1))

		def __repr__(self):
			return self.greeting + " " + self.object + " -- " + self.trans
		
	g = Greeting()
	print serialize(g)

