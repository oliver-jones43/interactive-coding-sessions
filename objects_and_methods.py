this_is_an_integer = 10
this_is_a_string = "Oliver"
type(this_is_a_string)
type(this_is_an_integer)

# After creaing a variable in python, you can check all. the things 
# that are contained in that variable using the "." in VScode
# Two things in the dot: 
# 1. Properties: signaled by the wrench icon, contains info, data.
# 2. Methods: signaled by purple box. describes all the actons that can be performed by the object
print(this_is_an_integer.numerator) # 10 
print(this_is_an_integer.denominator) # 1
print(this_is_an_integer.real)
# Properties describe the state of the object that we created.
another_integer = 5
print(another_integer.numerator)

# What about string properties?
print(this_is_a_string) # no general properties for a string
# Methods are much more useful
# they allow us to do stuff with the objects that we created
# functions bound to the object

# some methods: 
this_is_a_string.upper() # a method requires () because they are actions
# upper() translates everything to uppercase
# all strings will have this method. All objects of a given type share the same methods
this_is_a_string.lower() # everything is now lowercase

#let me show you a few more methods for strings
# strings can contain a lot of methods 
# because there are a lot of things that we can do with them
#we've already seen upper(), lower(), title()
my_sentence = "hello, my name is oliver"
my_sentence.title()
# we've also seen endswith(), let me show you a few more
lots_of_white_space = "        oliver "
lots_of_white_space.strip()
# let me show you a practical example of how these methods can be useful 
entry = "   oljo1134@colorado.edu.   "
# this is something someone could enter into a form
is_it_edu = entry.endswith("edu") # false. because we didnt strip the space
stripped_entry = entry.strip()
is_it_edu_fr = stripped_entry.endswith("edu") # now it will be true
# lets write it more cleanly

is_it_edu_clean = entry.strip().endswith("edu")
# This is called CHAINING. you can call methods on an object that is returned by another method

# Common Errors with Methods and Properties
entry.shout() # AttributeError: no attribute shout()
# you cannot call a method that doesn't exist on the object
price = 12
price.numerator() # TypeError: int object is not callable
# failing because an integer doesn't do anything. It is not a function or method.
# IT was attempting to call a property. You can only call a method inside an obejct

# a few more explorations
price.is_integer # this is a method. Purple box and an action
# we need the parenthesis to call the method! otherwise it won't do anything
price.is_integer() # True

# so far we've seen four big types of objects:
# str, float, int, bool
# In Python, you are often going to create other objects 
# let me show you an object that is going to solve a problem we'bve had before

from decimal import Decimal # not seen yet, soon! dw
# what is Decimal? it is a factory to make new objects. Decimal objects
# to create a str, you only need to put quotes
# to create a Decimal object, we are going to use the decimal thing we just imported
a = Decimal(".1")
type(a)
b = Decimal(" .2")
type(b)
print(.1 + .2) # what do we get? a FloatingPointError
print(a + b) # if you print the sum of two decimal objects, you get an exact representation
# Decimal solves this problem
# if you reach into a Decimal object with the dot, you are going to see a lot of new methods and properties
