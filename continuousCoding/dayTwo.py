x = 5 #x is of type int
y = "Hello" #y is of type string
z = int("123") #type casting
print(type(z))
#string variables can be declared either using single or double quotes

#variable names are case sensitive
a = 4
A = "Sal"
print(a)#A will not overwrite A

#variable names cannot begin with a number
#variable names cannot have a hyphen
#variable names cannot have space inbetween 

#camel case
myVariableName = "Aravind"

#pascal case
MyVariableName = "Kavya"

#snake case
my_variable_name = "Other"

print(MyVariableName)

#we can assign many values to multiple variable
d, e, f = "Test", 123, "Abc"
print(d)
print(e)
print(f)
#Also we can assign one value to multiple variables

#unpack a collection
fruits = ["apple", "banana", "orange"]
g, h, i = fruits
print(g)
print(h)
print(i)

#Global variables
i = "Global V"

def myfunc():
    print(i)

myfunc()

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

""" 
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""