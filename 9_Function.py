"""
Instead of making same process again and again there is a simple way
to give input to a function and process it and gives the desired
value in return.
"""

#pass command does nothing and just to make a function.
def Pass_Function():
    pass

#Shows the function location.
print(Pass_Function)

#It show None becouse function didn't return anything.
print(Pass_Function())

#Executes when function calls below the function declared.
def default_Print_Function():
    print("Hello, World.")

#Function call.
default_Print_Function()

#Shows number of none 
print(print(print(print("hello"))))

#Returning from functions
def Function():
	return "This is function!"
print(Function(),Function().upper())

#Sending values to functions
def Greetings(name):
	return "hi! {}.".format(name)
print(Greetings("Routh.kiran").upper())

#Placing default string in functions
def Greetings(name,AnotherGreetings="How are you"):
	return "hi! {}, {}.".format(name,AnotherGreetings)
print(Greetings("Routh.kiran").upper()) 
print(Greetings("Routh.kiran","How do you do").upper())

#Changing the default string in the functions
def Greetings(name,AnotherGreetings="How are you"):
	return "hi! {}, {}.".format(name,AnotherGreetings)
print(Greetings("Routh.kiran",AnotherGreetings="How do you do!").upper()) 

#Creating tuples and dictinaries by functions
def Student_info(*Tuple,**Dictionaries):
	print(Tuple)
	print(Dictionaries)
Student_info("My name","is kiran",name="Kiran",age="19")

#Testing for above function
def Student_info(*Tuple,**Dictionaries):
	print("Testing"+str(Tuple))
	print(Dictionaries)
List=["name","fame"]
Dict={"Name":"Kiran","Fame":"Student"}
Student_info(List,Dict)
Student_info(*List,**Dict)

#Program for leap year
Month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year(Year):
	return Year %4==0 and (Year % 100 != 0 or Year % 400 == 0)
def days_in_months(Year,Month):
	if not 1<=Month<=12:
		return "Invalid month!"
	if Month==2 and leap_year(Year):
		return 29
	return Month_days[Month]
for x in range(1998,2009):
	print(leap_year(x))
	for y in range(1,12):
		print(days_in_months(x,y),end=" ")
	print()
