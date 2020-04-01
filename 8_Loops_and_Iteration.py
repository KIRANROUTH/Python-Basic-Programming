Number_List = [1, 12, 321, 21]

for number in Number_List:
    print(number)

#Deleting the variable.
del Number_List

"""
Make a list with using forloop and find the element using forloop use
break statement.
"""
Number_List = [element for element in range(1,11)]

Finding_Element = 6

for index, element in enumerate(Number_List):

    #Instead of is you can use comparison operator (i.e., ==).
    if element is Finding_Element:
        
        print("{} is found {}.".format(Finding_Element, index))

        #Breaks the Whole loop.
        break
        
    print("{} is not {} at {}.".format(Finding_Element, element, index))

del Number_List, Finding_Element

#Use of continue statement.
Number_List = [2*element for element in range(1, 11)]

for number in Number_List:
    
    if number < 11:
        
        print(number)

        #Skips the below portion.
        continue
    
    if number >  10:

        """
        Please note that it does'nt continue so it will print the
        element twice.
        """
        print(number)
        
    print(number)

"""
#
Without using enumerate and global variable for displaying index and
element using nested for loop and continue and break statement.
"""
Number_List = [x for x in range(11)]

for number in Number_List:
    
    for character in "abcdefghijk":
        _number = number
        
        if number > _number:
            continue

        print("{} is found at {}.".format(character, number))
        number += 1

    if number > len(Number_List) - 1:
        break

#Print even number element from 5 to 20.
#6 is the starting number and 21 is not included and 2 is the step.
for number in range(6, 21, 2):
    print(number)

#The above code is also writen in while loop.
start_Number, end_Number, Step = 6, 21, 2

while end_Number > start_Number:
    print(start_Number)
    start_Number += Step

print("", start_Number, sep = "\n")

#Breaking the infinite Loop.
start_Number = 6
while True:
    
    print(start_Number)
    start_Number += Step
    
    if start_Number > end_Number:
        print("Stops here.")
        break
