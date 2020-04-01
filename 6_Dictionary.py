"""
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets,
and they have keys and values.
"""

Python = {
    "Designed by" : "Guido van Rossum",
    "Typing" : "Duck, Dynamic, gradual",
    "First appeared" : 1990,
    }

print(Python)

print(Python["Typing"])

#Key value is not present inside the dictionary.
print(Python.get("C++"));print(Python.get("Designed by"))

#Making .get to not give None as response.
print(Python.get("C++", "Not Found!"))

#Sys module importing.
import sys

#Displays python version.
print(sys.version)

#Converting the system version to string.
Python["Sys version"] = str(sys.version)

print(Python)

Hacker = {
    "Name" : "xyz",
    "Born" : 1998,
    "Needs" : "Money"
    }

#Update changes the key and also adds new key and value.
Hacker.update({
    "Name" : "abc",
    "Born" : 2002,
    "Primary Need" : "Save World!"
    })

print(Hacker)

#Showcasing all the keys in Dictionary.
print(Hacker.keys())

#Showcasing all the values in Dictionary. 
print(Hacker.values())

#Showing the all keys and values in form of tuples inside the list.
print(Hacker.items())

for key, value in Hacker.items():
    print(key + " -> " + str(value))

del Hacker["Needs"]

print(Hacker)

Need = Hacker.pop("Primary Need")

print(Need, Hacker, sep = "\n")

#Showing the number of items.
print(len(Hacker))
