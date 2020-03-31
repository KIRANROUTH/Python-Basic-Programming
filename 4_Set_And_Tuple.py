#Sets dont have index value to get the element like list.
#Set can also be initial as {}.
Number_Set, Set_Initial = {1, 1, 3, 12, -5}, {}

print(Number_Set, Set_Initial)

#Sets dont have same element more than once.
print(Number_Set)

#To check element in Set present or not.
print(5 in Number_Set)

Number_Set_1 = {1, 2, 3, 4}
Number_Set_2 = {3, 4, 5 ,6, 6}

#Checking the initial set intersecting the other set.
print(Number_Set_1.intersection(Number_Set_2))

#Checking the difference in elements compared to other set.
print(Number_Set_1.difference(Number_Set_2))

#Combining the two sets.
print(Number_Set_1.union(Number_Set_2))

#Tuple have index embadded in the elements but cant be changable.
Number_Tuple, Tuple_Initial = (21, 12, 33, 87), (1,)
print(Number_Tuple[0], Tuple_Initial)

"""
To change the value of tuple element you can cange tuple into List
if necessary and can easily change back to tuple for not changing the
value.
Conversion between tuple, list and set."""

List = list(Number_Set)

print(type(List))

Set = set(List)

print(type(Set))

Tuple = tuple(List)

print(type(Tuple))

print(List, Set, Tuple, sep = "<->", end = "\n")





