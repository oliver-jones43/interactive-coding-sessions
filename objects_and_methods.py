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
