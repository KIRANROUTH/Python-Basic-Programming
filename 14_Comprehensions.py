#Just copping the list or dulplication
n=[1,2,3,4,5,6]
l=[]
for item in n:
	l.append(item)
print(l)

#The above for loop can be written as
num=[item for item in n]
print(num)

#Squaring each element
n=[1,2,3,4,5,6]
l=[]
for item in n:
	l.append(item**2)
print(l)

#The above for loop can be written as
num=[item**2 for item in n]
print(num)

#Map runs every thing of certain range of function
#Does the same as above code
List=map(lambda n: n**2,n)
print("Location: "+str(List))
List=set(List)
print("Using map and lambda: "+str(List))

#This function is used for multiple or divisible by two
num=[]
for item in n:
	if item%2==0:
		num.append(item)
print(num)

#Above forloop can be written as 
n=[1,2,3,4,5,6]
i=[item for item in n if item%2==0]
print(i)

#Does the same as above three statements
mylist=filter(lambda n:n%2 ==0,n)
print("Filter location: "+str(mylist))
mylist=set(mylist)
print("Mylist: "+str(mylist))

#Making each letter corresponds to range 0 to 3
n=[]
for letter in "abcd":
	for num in range(4):
		n.append([num,letter])
print(n)

#Does same output as before
n=[[num,letter] for letter in "abcd" for num in range(4)]
print(n)

#Creating a dictionary having pair of element in tuple
name=['Bruce','Clark','Peter','Logan','Wade']
Hero=['Batman','Superman','Spiderman','Wolverine','Deadpool']
Set=set(zip(name,Hero))
print(Set)

#Just making a dictionary
dicti={}
for name,Hero in Set:
	dicti[name]=Hero
print("Dictionary: "+str(dicti))

#Just same output as before
Dict={name:Hero for name,Hero in Set}
print("Comprehension: "+str(Dict))

#For not including peter key and value in dictionary
Dict={name:Hero for name,Hero in Set if name!="Peter"}
print("Comprehension: "+str(Dict))

#Use of set is stops repetation
List=[1,1,1,2,3,4,4,5,6,7,7,7,6,3,4,5,6,7,7]
Set=set()
for n in List:
	Set.add(n)
print(Set)

#Above comprehension is
List=[1,1,1,2,3,4,4,5,6,7,7,7,6,3,4,5,6,7,7]
Set={n for n in List}
print(Set)

#Generators and yield commands
num=[1,2,3,4,5,6,7,8,9,10]
def Generator(num):
	for n in num:
		yield n*n
My_gen=Generator(num)
for i in My_gen:
	print(i,end=" ")

comp=(n*n for n in num)
print(comp)
for i in My_gen:
	print(i,end=" ")