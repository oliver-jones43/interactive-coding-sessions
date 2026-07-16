print("hello, world")
print(2+2)
# Here, nothing gets executed when I press enter
#How can I run this code?
# two ways:
# 1. you can put the caret on the lone and press shift enter
# 2. just run the file 
# you will want to do this once you finish writing your script
# reminder 1: we can create variables in python and assign a content to them:
my_name = "Oliver Jones"
print(my_name)

# four big data types:
this_is_an_integer = 10
this_is_a_float = 3.14
this_is_a_string = "hello world!"
this_is_a_boolean = True

# Print function
# We can print multiple things at once, separated by a comma

# A function is an action

# you can print:
# a value:
print(3.14)
print("hello world")
# a variable:
print(my_name)
# an expression, something that has not been calculated yet
print(2+2)
# Reminder: expressions are calculated inside to out
# SKILL: when reading code, try to always understand what is going to happen and in which order
print(this_is_an_integer + 5) # trace: Reads values, adds variable and 5, then prints

# How do you figure out the type of the variable?
what_is_this =type(this_is_an_integer)
what_is_that = type(3.12)
print(what_is_that)

# Calculations : 
print(2 + 3)
print(2 + 5*3)
print((2+3)*5)
print((1+2) == 3) #logical comparison: will print true if correct or false if not
print(0.1 + 0.2) # what happened?
print((0.1 + 0.2) == 0.3) # We get a false because Floating Point Error: 
# Do not expect float operations to be exact
# what can you do?
my_rounded_addition = round((0.1 + 0.2), 1) #rounds to nth digit, in this case 1
print(my_rounded_addition) # now you get 0.3
# a round with no nth digit goes to 0 if not specified

# Logical Comparisons: 
print(3 == 5) #equality
print(3 != 5) # not equal
print(3<5) # greater
print(3>5) # less
print(3<=5) # less than or equal to, >= greater than or equal to

# you can combine logical comparisons writing AND or OR

condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #True
print(condition_1 and condition_3) #False
print(condition_1 and condition_2 and condition_3) #False has to all be true
print(condition_1 or condition_2) #True
print(condition_1 or condition_3) #True because OR returns True if one condition is True

# lets do a few more calcs:
print(True + True) # you get 2 because True == 1 False == 0
print(True * 5) # you get 5 because True is 1
print(10/0) #error because cannot divide by 0, or False for that matter

# lets do some string manipulation. 
# calculate with strings
greeting = 'hello' + 'world'
print(greeting) # works because of concatenation: bringing things next to each other
laugh = 'ha' * 3
print(laugh) # for strings, * means repeat string x number of times

weird_laugh = 'ha' * 3.12 # type error: you cannot multiply a string by a non integer

# How do we keep things simple? we make sure to convert variables before working with them
number = 42
is_this_a_number = "42"
print(number + 10)
# if you attempt to add a number to a string, you get an error
print(is_this_a_number + 10) #type error: string plus integer so it wont work
# create a new variable: 
now_this_is_a_number = int(is_this_a_number) #int turns something that is not a number into a number
print(now_this_is_a_number)
# what would I get if I typed this?
int("fifteen") #value error. sequence of letters cannot be turned into an integer
int(False) # you get zero! this one works

# one more example. 

my_age = 39
my_intro = "Hello, my name is Quentin and I am " + my_age
# wont work once agian because you can only concatenate strings together
# convert my_age to string by doing str(my_age)
# str(), float(), int(), and bool() are functions that can turn an input to a desired type
