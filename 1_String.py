Message = "Hello World."

#Prints the message.
print(Message)

#Makes the message to upper case.
print(Message.upper())

#Makes the message to lower case.
print(Message.lower())

#Notice the message 2 has \symbol for single quote message.
Message_1, Message_2 = "It's real.", 'It\'s not real.'

print(Message_1, Message_2)

Message = "Welcome to my World."

#Prints number of W in Message variable otherwise 0.
print(Message.count('W'))

"""To find the position of y in Message. Indexing starts from 0.
 Otherwise -1."""
print(Message.find('y'))

New_Message = """This is multi-line
comment."""

print(New_Message)

Message = "Hello World."
#Replacing the word in message.
New_Message = Message.replace("World", "Friend")

print(New_Message)

Message_1, Message_2 = "I like ", " country."

#Addition takes place when all the variable must have same type.
Full_Message = Message_1 + "my" + Message_2

print(Full_Message)

number_Three, number_Four = 3, 4

#Converting to string from other type.
string_Three, string_Four = str(number_Three), str(number_Four)

print(string_Three + " and " + string_Four + " are strings.")

Name, Does = "JB", "Programming"

#Putting a value of varible into string.
print("My name is {} and I does {}.".format(Name, Does))

#Note where do .find, .replace, and .count functions stays
print(dir(Message))
print(dir(Message.replace))


