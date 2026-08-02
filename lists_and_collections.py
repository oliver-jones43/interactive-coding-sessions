# Talk about collections. Collections are objects designed to hold other objects inside them
# They are like bags of different kinds

# Lists

# a list is an ordered collection of items
# it is created using square brackets []

my_empty_list = [] # list that doesn't contain anything
type(my_empty_list) # a list! a new type of object

# what do lists do? They contain other objects

my_favorite_numbers = [1,2,3,4,5]
print(my_favorite_numbers)

# Lists can contain other elements 
my_favorite_colors = ['red', 'blue', 'green'] # list of strings for example
my_fav_decimals = [3.1, 3.2, 4.6] # list of floats
my_fav_bools = [False, True, False] # list of booleans

# lists can contain different elements of different kinds
my_fav_things = ['red', 3.14, 2, False] # literally anything you want

# even other lists

my_mixed_lists = [False, ['blue', 19], ['red', False], 3.14]

# lists are objects meanings...
# they contain properties and methods

# methods of lists

my_favorite_colors.append('yellow') # ['red', blue', 'green']
print(my_favorite_colors) # now its got yellow

# this method 'append' is so much different from other string methods, because it changed the object

my_string = 'Oliver'
my_string.upper() # I run this... but if I print the original string it will still be in lowercase
# The method copies the original object, changes it, then returns the copy

# This is because strings are immutable. once created, their content will not change
# the oinly way to make changes to a string is to create a new one with a different content

# back to lists: lets see how methods affect them

a = my_favorite_colors.append('pink') # now contains ['red', 'blue', 'green', 'yellow']

# the method changed the object, adding pink, but now what is in a?
print(a)
# nothing. When you are working wit ha moethod that mutates the original, it will typically not return the original
# it will simply do something to the original, but then return None

# let's say we dont like that. We dont like that every time we are adding 
# things to my favorite colors, it changed the original

my_original_colors = ['pink', 'purple']
# I want to add a color to this list, but not modify the original:
my_updated_colors = my_original_colors # I want this to be my backup
# now I can add something to my_updated_colors and my_original_colors won't change, right?
my_updated_colors.append('orange')
print(my_updated_colors)
print(my_original_colors) # EH wrong. it changed because you set the two objects equal to each other
# this is because lists are mutable, so even if given different names it still changes
# you need to use the copy method if you want it to actually not change

# Other methods with lists

my_favorite_colors # ['red', 'blue', 'green', 'yellow', 'pink']
# lets remove an element of this list
removed_color = my_favorite_colors.pop() # pop removes the last element of the list
# what will be the content of my_favorite_colors?
print(my_favorite_colors) # this contains everything else
print(removed_color) # now this contains only pink

# what if I rerun this line?
removed_color = my_favorite_colors.pop() # it will remove yellow, then yellow will be assigned to removed_color
print(my_favorite_colors)
print(removed_color) # pink is gone though. just fyi

# what happens if you don't assigned the popped color?
my_favorite_colors.pop() # list now contains [red, blue, green]
# 'green' goes into the terminal. If a function or method returns something, and we don't catch it, it falls into the terminal

# lists are ordered. meaning you can reach into them at a specific position and grab the content

my_favorite_names = ['oliver', 'quentin', 'joe']
# lets say I want what is at the beginning of the list: 
# if you want an element, you can use an operation called INDEXING
# indexing is: you put [], after the list, and use the INDEX of that element
# that you want to grab:
print(my_favorite_names[0]) # You get oliver

# what happens if you index an element that isnt there?
print(my_favorite_names[3]) # IndexError: out of range

# lets continue our discussion of indexing
# what if we do negative?
print(my_favorite_names[-1]) # -1 reads the last in the list, -2 is second to last, so on and so forth

# we can also do something called SLICING to grab multiple values
# from a list: 
my_favorite_numbers = [1,2,3,4,5,6,7,8,9,10]
my_favorite_numbers[2] # third value
# the syntax for slicing is [start:stop:step]
my_favorite_numbers[0:3:1] # this means all the values between the first and the fourth (excluded) and all of them
my_favorite_numbers[1:6:1] # all values between second and seventh (excluded) and all of them
my_favorite_numbers[3:8:1] # all values between the fourth and 9th (excluded), and all of them
my_favorite_numbers[0:6:2] # 1 3 5. all values between first and seventh (excluded), and every second value

# when you are sliving you can omit some arguments:
my_favorite_numbers[0:3] # by default, step is 1. 
my_favorite_numbers[1:] # All of them starting from the second. defaults until end of list, step is one
my_favorite_numbers[:4] # starting from the first up to the fifth (excluded)
my_favorite_numbers[::2] # start and stop are omitted, so its jsut gonna be every second value of the list
my_favorite_numbers[::-1] # it counts down from the top of the list

# want to see something cool?
my_name = "Oliver Jones"
my_name_but_mirrored = my_name[::-1]
my_name_but_mirrored # you can slice strings too 
my_name[0:4] # first to fifth (excluded)

# So far we learned that lists are mutable, meaning we can modify their content using methods
# Lists are Iterable, meaning we can select a subset of their content using slices

# lets put this together
my_favorite_names # lets replace 'oliver'
my_favorite_names[0] = 'jaxonwaxonflaxonyappin' # we are indexing the first element of the list, and assigning it a new thing
my_favorite_names

# we can do the same thing with slices
my_favorite_names[1:] # this is slicing second to third names
my_favorite_names[1:] = ['jimmy', 'george']
my_favorite_names # we can use slicing to read or update the contnent of the list

# Bonus question: can we use indexing or slicing to update the contnet of the string?
my_name[0] = "z" # Nope. Strings are not mutable. 

# back to a few list methods:
my_favorite_names.pop() # removes the last element of the list
my_favorite_names.append('jacob') # add this element to the list
# pop and append can take an additional argument: the position
my_favorite_names.pop(0) # first item
my_favorite_names.insert(0, 'Adam')
my_favorite_names # all these methods are modifying the original list nit returning the copy of the list
my_favorite_names.reverse() # what will this return? Nothing. It changes the order of the list
my_favorite_names 

# lists are a collection of ordered items
# Dictionaries are a collection of key:value pairs

my_friends_age = {'Nick': 40, 'Sam': 35, 'Juan': 37}
# dicitonaries have {} syntax

#dicitonaries can have different types of values: 
my_information = {'name':'Oliver', 'age': 22, 'hobbies': ['hockey', 'hiking', 'skiing']}
# key name contains a string value
# key age contains an integer
# key hobbies contains a list

# keys are typically str or int. The most important rules:
# 1. they HAVE to be unique (only one key must have a given name)
# and they have to be IMMUTBALE

# how do we use dictionaries?
# we can INDEX them like lists
my_friends_age['Nick'] # will this give us nicks age?
# yes. we got 40. you index by the key words
my_information['hobbies'] # you get every value in the hobbies key

# dictionaries like lists are mutable. we can update them
# nick is older, lets change his age
my_friends_age['Nick'] = 41 # did not return anything
my_friends_age # now nick is 41 instead of 40

# lets try another example.

# can I change my name to Oliver Jones?

my_information['name'] = 'Oliver Jones'
# we can add new keys
my_information['job'] = 'student'
my_information # now it has job as a new key word with value student

# we can use indexing to: 
# 1. read the value of an existing key
# 2. update the value of an existing key
# 3. create a key with a given value.

# since dictionaries are objects, they have methods! 
# first useful method :get()
# if you idnex a dictionary with a value that does not exist, what happens?
my_information['address'] #KeyError: key doesnt exist
# errors stop script at the error
# a better way to check if a key exists is the get() method
my_information.get('address') # returns nothing back. 

# three other useful methods: rather than blindly checking if a key exists, sometimes you want to see all the keys
my_information.keys() # returns every key in the dictionary
# you. can do the same thing to see all the values with .values()
my_information.values() 
# you can now know all the keys and values, but you don't know which corresponds to what
my_information.items() # everything and their pairs

# two more things about dictionaries: reminder key of dicts must be ints or strs

# something common is to have dicts as values to store more complex info
my_friends_info = {
    'Nick': { # one key: Nick, one value: his dictionary
        'age': 41,
        'city': 'Boulder',
        'hobbies' : ['skiing','cooking']
    }, 
    'Sam': {
        'age': 35,
        'city': 'Chicago',
        'hobbies': ['hiking','coffee'],
        'job': 'professor'
    }
}
my_friends_info['Nick']['age'] # now you just get 41
# lets get sams hobbies
my_friends_info['Sam']['hobbies']
# what if your not sure if you have info about a friends job?
my_friends_info['Nick'].get('job') # we get nothing because no such keyword in the dict
my_friends_info['Sam'].get('job') # we get professor for Sam
# sam recently picked up bird watching
my_friends_info['Sam']['hobbies'].append('Bird watching')
my_friends_info # boom its modified because we can change lists

# Lists are ORDERED collections of elements of any kind.
# we manipulate lists using INDEXING OR SLICING ot access  and modify the elements that they contain
# we can also use methods like .pop(), .append(), or .insert() to do that.

# Dictionaries are UNORDERED collections of key:value pairs
# we access the values by their key
# we manipulate dictionaries using INDEXING to access and modify the values associated with given keys

my_friends_info[0] # nothing, no key called 0