# Introduction to Python
# Adam Tilson
# These exercises will be similar to those from ENSE 350, Lab 1

# print hello world
print ("Hello World!")
print("")

print("some basics with numbers")
print ()

print("simple numerical operations")
print (1+1)
print (3*4)
print("")

print("float division by default")
print (1/3)
print ()

print("quotients and remainders")
print (17//5, 17%5)
print("")

print ("string operations")
print ()

print("strings and concatination")
print ("hello" + ' ' + """World""")
print("")

print ("string repitition")
print ("hello" * 5)
print("")

print ("string slices")
print ("hello world"[3:7])
print ()

print ("list operations - list are mutable data structures")
new_list = [1,3,7]
print (new_list)
print ()

print ("all list functions")
dir (new_list)
print("")

print ("help on all list functions")
print ("help (new_list.insert)")
print ()

print ("appending lists")
new_list.append(9)
print (new_list)
print ()

print ("tuples are immutable data structures")
tuple_t = (1,3)
print (tuple_t)
print ()

print ("Reading element 0")
print (tuple[0])
print ()

print ("Trying to write element 0")
try :
    tuple[0] = 3
except TypeError:
    print ("tuples do not support assignment!")
print ()

print ("Dictionaries rock. Keys are immutable, values are mutable.")
dict_d = {"a": "aqua", "b": "blue", "c":"cyan"}
print (dict_d)
print ()

print ("Changing the values for existing keys.")
dict_d["a"] = "alizarin"
dict_d["b"] = "burgandy"
dict_d["c"] = "crimson"
print (dict_d)
print ()

print ("Branching in python - mind your indentation!")
x = 4
if (x == 4):
    print ("x is 4")
elif (x == 5):
    print ("x is five")
else:
    print ("x is neither 4 nor 5")
print ()

print ("Looping - for each style")
ordered_list = [1,2,3,5,7]
for number in ordered_list:
    print (number)
print ()

print("Also supports while loops")
i = 0
while i < 3:
    print (i)
    i += 1
print ()

print("And range-based for loops")
for i in range(6):
    print (i)
print ()

print("Functions exist in python")
def square (x):
    return x*x
print (square(3))
print ()

print ("It even supports object-oriented programming")
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def getNameAndAge (self):
        return self.name, self.age

    def setAge (self, age):
        self.age = age

Adam = Person("Adam", 50)
name, age = Adam.getNameAndAge()
print (name, age)
print ()

print("python can be extended with libraries")
import math
print(math.sqrt(9))
print ()