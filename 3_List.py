"""The content can be chaged without changing the identity are called as
mutable. The objects like lists and dictionaries.

The content that cannot be changable called as immutable. Example like
string and tuples"""

#List formation.
Fruit_List = ["Apple", "Banana", "Mango"]

#Finding the length of list.
Fruit_List_Length = len(Fruit_List)

print("The length of {} list is {}.".format(Fruit_List,
                                            Fruit_List_Length))

'''Prints first element of list having an index of 0;
Last element is represented with index -1'''
print(Fruit_List[0]); print(Fruit_List[-1])

#To get first two elements from list.
print(Fruit_List[0:2])

#Adding new elements to the list at last position by default.
Fruit_List.append("Grapes")

print(Fruit_List)

#Adding new element to the index of 1.
Fruit_List.insert(1, "Orange")

print(Fruit_List)

#Making a sub list.
eatable_List = [["Potato", "Carrot"],["Glucose", "Energy drink"],
                "Chocolate", "Ice Cream"]
eatable_List.insert(1, Fruit_List)

print(eatable_List)

#To get the banana the indexing would be.
print(eatable_List[1][2])

""".remove function happens for sub list compared with other list.
not for Marvel_Character.remove(DC_Character)."""
eatable_List.remove(Fruit_List)

print(eatable_List)

eatable_List.remove("Chocolate")

print(eatable_List)

Marvel_Character = ["Iron man", "Captain America", "Spider man"]
DC_Character = ["Bat man", "Super man", "Wonder women"]

#Appending all the elements of other list by extend function.
Marvel_Character.extend(DC_Character)

#Not making a sub list.
print(Marvel_Character)

Integer_List = [1, 2, 3, 4, 5]

"""pop function removes last item it can also return value of removed
item"""
Integer_List.pop()

print(Integer_List)

Last_Item = Integer_List.pop()

print(Last_Item)

Game_List = ["Foot Ball", "Basket Ball", "Tennis", "Chess",
             "Carrom Board"]

#Reverse function reverses the element index in the list.
Game_List.reverse()

print(Game_List)

Game_List.sort()

print(Game_List)

Game_List.sort(reverse = True)

print(Game_List)

#Gives the same list as sorted list but not in reverse way.
Original_Old_Game_List = sorted(Game_List)

print(Original_Old_Game_List)

Number_List = [5, 3, 7, -1]

BigNumberInList, SmallNumberInList = max(Number_List), min(Number_List)
SumOfElementInList = sum(Number_List)

print(str(BigNumberInList) + ", "
      + str(SmallNumberInList) + " and " + str(SumOfElementInList))

Animal_List = ["Lion", "Tiger", "Bengal Tiger"]

#To find element index in the list otherwise valueerror occurs.
print(Animal_List.index("Bengal Tiger"))

#To check the element present in the list otherwise False.
print("Lion" in Animal_List)

"""Making the List into the string by having a special character
in between."""
Animal_List_String = "-- ".join(Animal_List)

print(Animal_List_String)

Old_Animal_List = Animal_List_String.split("-- ")

print(Old_Animal_List)
