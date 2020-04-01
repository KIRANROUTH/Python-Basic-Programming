'''
#Importing used made module in same directory as the rename called Module
import Mymodule as Module

#Line 17 is written as [index=Module.Find_Index(courses,'physics')]
'''

#Importing only Find_Index and Test from Mymodule or can be written as 
#from Mymodule import *
from Mymodule import Find_Index as FI,Test as T

#Creating a list
courses=['History','math','physics','compsci']

#Calling a module inbuilt function
#Sending list name courses and the element to the function
index=FI(courses,'physics')

print(index)
print(T)

'''
To know how to set a module as global means we can import from any location
See the link: https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9
From time: 11:44 to 13:8
'''

