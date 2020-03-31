"""
Create a List of elements from 1 to 10 without using comma and
print the odd elements in the if statement is true for element is even
using for loop.
"""

Number_List = list(x for x in range(1, 11))

for element in Number_List:
    if element%2 == 0:
        print(element - 1)

"""Print the index and elements in the list using enumerate."""

Number_List = list(x for x in range(20,41))

for index, element in enumerate(Number_List):
    print(index, element)

"""
Print elements of the list with index starts from 5 using enumerate.
"""

for index, element in enumerate(Number_List, start = 5):
    print(index, element)

"""
Creat a tuples inside a list having two different letters of
word/sentence.
"""

Word, ListHavingTuples = "Hill Station", []

for TupleIndex_0 in Word:
    for TupleIndex_1 in Word:
        if TupleIndex_0 != TupleIndex_1:
            Tuple = (TupleIndex_0, TupleIndex_1)
            ListHavingTuples.append(Tuple)

print(ListHavingTuples)

