# Control flow is a term describing all the tools in Python that govern whether, when, and how 
# much/often a block of code is going to run. Up until now, every line that we were writing
# was running

# first up: conditional logic.
# this is what governs whether a block of code is going to be executed.
my_name = "oliver"
my_gender = "male"

if my_gender == "male": # A conditional logic block always starts with "if"
# followed by a "condition". It is a statement that will evaulate to True or False
# The line ends with a colon ":", then the line below you start an indented block: 
# this indented block describes the lines of code that will run ONLY if the condition evaluates to True
# for the most simple conditional logic block, that's all you need. 
# a block with just one IF is binary: either the block geets exectued (if CONDITION is True)
# or it isn't (if CONDITION is False)
    print("hello Mr" + my_name) #Sometimes the world is more complicated. There's more than one possibility.
    #That's where you can add some bells and whistles to your conditional block.
    #using the keywords elif and else
elif my_gender == "Female": #elif is shot for else if
    #it describes a second possible condition
    #that is ONLY going to be checked if the previous cdonditions evaluated to False
    # It's sequential: we start from the top,
    #we check is the firt condition is True,
    #if it is true, we end here.
    #If it is 
    # False, we check the second condition
    #If it is False again, we check the third condition...
    #We can have zero, one, or many 'elif' statements
    #allowing you to check additional specific conditions
    print("Hello Mrs" + my_name)
elif my_gender == "Non-Binary":
    print("Hello " + my_name)
else: #Then, at the bottom, after all the elid statements (if any)
    #we can have the 'else' block. The else block means:
    #if ALL the conditions turned out to be False,
    #gere's what you should do
    print("Hello " + my_name + ", how should we address you?")
#If there is no else statement, nothing happens when all the other conditions
#evaluate to FALSE

# a very common gotcha condition logic issue:
# Conditional Logic Blocks are very common inside functions:
#they allopw you to have functions that haver a different behavior as a function of their inputs:

def status_checker(age):
    # we want this function to return the status of the user as a function of the age they specify
    if age >= 13:
        return "you are a teenager"
    elif age >= 18:
        return "you are an adult"
    elif age >= 4: 
        return "you are a child" 
    elif age >= 2:
        return "you are a baby"


# lets check
status_checker(1)
status_checker(4)
status_checker(14)
status_checker(39) # huh? I am a teenager?

def correct_status_checker(age):
    if age >= 18
        return "you are an adult"
    elif age >= 13:
        return "you are a teenager"
    elif age >= 4:
        return "you are a child"
    else:
        return "you are a baby"

correct_status_checker(39)
    


    