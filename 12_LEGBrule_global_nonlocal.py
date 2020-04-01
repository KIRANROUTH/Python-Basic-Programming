'''
LEGB
Local, Enclosing, Global, Built_in
This means that python first search for local, then Enclosing ,and so finally built_in
'''

#Importing a module for builtins
import builtins

#To print all the built in variables
print(dir(builtins))

#Making a global variable that can be extracted by all function and other type
x="Global value"

def FunctionN():
	#Created a local string that can't be extracted away from the function
	y="Local value"
	print(y)

print(x)

#Function call
FunctionN()


def Function():
	#Making y variable to be a global
	global y
	y="Local value"

#Function call
Function()

#Past value of y as Global value changed to Local value this is done when we call function
print(y)

#Making a function that takes and prints where v is local
def Function2(V):
	print(V)
Function2("Message")

#Built in function or variable
m=min([1,2,3])
print(m)

#Making an enclosing variables
def Outer():
	x="Outer value"
	def Inner():
		x="Inner value"
		print(x)
	Inner()
	print(x)
Outer()

#Said as enclosing becouse if x value is not present in inner function then it checks to outer function
#Outer is the closing function and x="Outer value" is the enclosing variable
def Outer():
	x="Outer value"
	def Inner():
		#x="Inner value"
		print(x)
	Inner()
	print(x)
Outer()

#NonLocal command used to be a global variable is side the closing function
def Outer():
	x="Outer value"
	def Inner():
		nonlocal x
		x="Inner value"
		print(x)
	Inner()
	print(x)
Outer()
print(x)

#Function that is built in becomes global and does not do the min operation given below 
def min():
	pass
m=min([1,2,3])
print(m)