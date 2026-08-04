# lets talk about range().
# a FOR loop is iterating over a range of an iterable (counting over something)
for i in [1,2,3,4,5]: # i is the step variable the list is the iterable
    print(i) # i is going to take, in turn, the value of each of the elements in the iterable

# now imagine we want to get all the numbers from 0 to 1000:
# writing the loop the old way we do something like this:
for i in [1,2,3,4,5, 1000]: 
    print(i) # a bit of a pain to write
# so... enter range(). 
# Range is a function that creates an iterable for you that you can loop on
# range takes three arguments: start, stop, step
# start is optional and defaults to 0
# step is optional and defaults to 1

for i in range(1000,1): # all the numbers between 0 and 1001 excluded
    print(i)

# start stop step should remind you of slices. 
my_list = [0,1,2,3,4,5,6,7,8,9,10]
my_list[0:4]
my_list[::2]

for i in range(0,1000, 2):
    print(i)

# all there is to know about range: a convenient way of getting 
# an iterable of numbers to loop on.

# the final thing on loops I want to show you is something called
# list comprehensions.

# lets say I want the square of all the numbers between 0 and 9:
# lets write the loop that iterates over numbers between 0 and 9, take the square of each of them,
# and store them in a list called my_squares
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_squares = []
for i in my_numbers:
    square = i**2
    my_squares.append(square)

print(my_squares)

# this task, creating a new list from an existing iterable, is extremely common in python
# thats what a shortcut called LIST COMPREHENSION is doing
# here I could have done the same job by typing:
my_squares = [i**2 for i in range(10)]
# a list comprehension is surrounded by square brackets. this is because we are creating a list.
# Then you see an expression: i ** 2. this defines how the step variable is going to be modified
# to create the elements of the liste
# finally, you see the loop itself: for STEP_VARIABLE in ITERABLE. Note there is no colon here.
my_list = [x.upper() for x in "quentin"]
print(my_list) # a list of his name in all caps

# one final thing on list comprehension:
# we can add, after the (for STEP_VARIABLE in ITERABLE) an optional IF statement:

my_filtered_squares = [i ** 2 for i in range(10) if i ** 2 < 30]
print(my_filtered_squares)
# only add the to the list if the squares are less than 30

# very common use case for this filter:
paths = ['data.csv',  'report.pdf', 'summary.csv', 'iamge.png', 'notes.txt', 'data2.csv']
# lots of files of different types
# lets say we only want to keep the elements that have the extension 'csv'
my_csv = [i for i in paths if i.endswith('csv')]
print(my_csv)

# how could I write an equivalent for loop that would do the same job:
my_csv_loop = []
for i in paths:
    if paths.endswith('.csv'):
        my_csv_loop.append(i)