# we've been using functions from Day 1 (or almost): 
# print(), type(), etc. 

# a function is a MACHINE for doing something
# takes an input then returns a result

# print() <- takes any expression that we want to print
# it prints stuff to the user

# str() <- takes any expression and turns it into a string, and returns it to the user

# what does it mean to return something?
#mets take print(): 
print("1234") # it is going to print "1234"
my_content = print("1234")
my_content # this is empty. print("1234") did not store anything in it
# why? 

# some functions (most) return something. think of them as a conveyor belt:
# They are going to take an object on one side, do things to it, and then Return
# the result to the other side

# other functions are like an engine: you give them gas, and they are going to do something
# but they won't hand you back anything

# lets write functions together to better understand this distinction. 
# we are going to write a function that takes a price, a rate, and returns the price updated with rate


# we create a new function like this: 
def print_total(price, rate): # def, followed by function name, and in parenthesis are arguments
    # You will see that your curser moved to the right"
    # this defines the body of the function. every code inside will define what fxn does
    total = price * (1 + rate)
    print(total)

# we've created our functions, lets test drive it! 
print_total(10, 0.1) # lets run this and practice tracing the code
# lets say I want to store this result for later use: 
my_total = print_total(10, 0.1)
my_total # nothing inside my_total. This function is just an engine
# lets solve this issue
def calculate_total(price, rate): 
    total = price * (1+ rate)
    return total # on the other side of the conveyor belt, spit out the total
my_total = calculate_total(10, 0.1)
print(my_total) # success! this fxn calculated something, returned it back to me
# and now I can store it into a variable
# What happens if you don't store it? 
calculate_total(10, 0.1) # it just prints it into the terminal
# always better to have fxns RETURN stuff. gives more flexibility to user

# more vocabulary: the inputs of a function are called arguments: 
# two flavors: 
# 1. Posiitonal Arguments: defined by the order you present them in
round(3.14, 1) # Rounds the first number to the first number of digits in the second number
round(1, 3.14) # TypeError. Float object cannot be interpretted as integer
# the Position matters! 
calculate_total(0.1, 10) # doesn't return 11.0, order matters
# some fxns take a variable number of arguments 
round(3.14) # it will give you 3. the second argument is not compulsory. it has a default which is 0
print("abc")
print("abc", "def", "ghi") # it will print all three strings. print() is a function that
# takes an arbitrary number of arguments

# 2. Second flavor of arguments: 'named' arguments or keyword arguments
# these are arguments that are added by specifying their name:
print('a', 'b', 'c', 'd', sep="*") # here sep is a named argument and I give it value *
# named arguments are not compulsory, and have a default value. 
# default argument for sep is a space
print('A', 'B', 'C', 'D', sep='-', end='!')

# One final but important thing: 
def add_excitment(string): 
    excited_string = string + " !!!!!"
    return excited_string
yo_mama = add_excitment("yo mama")
print(yo_mama)
# if you try to add anything after a return statment, it will not do anything

print("hello")







