import numpy as np
import math
import pandas as pd
# first thing we are going to do is something we've done once of twice:
# import a library
# if a library is not installed, what do we do? UV! uv add pandas numpy
print(math.pi)
print(math.sqrt(9))

# lets talk about the arryas now. Arrays are a new kind of object that live
# in numpy package
my_array = np.array([1, 2, 3, 4, 5])
print(my_array) # looks a lot like a list
print(my_array[1])
print(my_array[0:3])
# so whats the difference really?
type(my_array)
# there are two fundamental differences
# 1. an array requires ALL its elements are the same type.
my_list = ['quentin', False, 32]
my_list[1] # bool
my_list[0] # str
my_array = np.array(my_list)
print(my_array) # every element became a string
# in technical term, we would say they were coerced to a common type.
# its a string because it is the most common type 

# because all elements of an array have the same type,
# arrays themselves have what is called a dtype, short for data type:
print(my_array.dtype) # U21
# other examples:
float_array = np.array([3.14, 2.16, 1.5])
print(float_array.dtype)
int_array = np.array([1,2,3])
print(int_array.dtype)

# second distinction between lists:
# Arrays have a FIXED SIZE
# you cannot add or remove elements from an array after it was created.
my_list = [1,2,3,4,5]
my_list.pop()
print(my_list) # the pop method has removed the last element of the list
my_list.append(6) # added an element
# what abouit arrays?
my_array = np.array([1,2,3,4,5])
my_array.pop() #AttributeError
my_array.append() #AttributeError
my_array.insert() #AttributeError. All the methods that allow you to insert remove or append an element
# in a list does NOT exist on arrays.

# Isntead you need to use functions to create new arrays:
my_bigger_array = np.append(my_array, 6) # this will create a new array that has the same content
# as my_array, plus the element 6 appended to the end:
print(my_array) # unchanged
print(my_bigger_array) # new array

# Summary: arrays are more constrained. They have to have the same data type and are fixed length

# These restrictions enable very powerful things:

# let me show you the world:
# First, lets not use the arrays:
prices = [9.99, 19.99, 4.99, 14.99, 24.99]
quantities = [120, 75, 300, 50, 40]
# say I want to calculate the total rev for each product. p*q
total = []
for (p,q) in zip(prices, quantities):
    total.append(p*q)
print(total) # you can't see it but this is slow af
# what arrays alloew you is to do VECTORIZED operations. Rather than taking the elements one by one
# and checking, one by one, if the operation is allowed and how it works, arrays are going to perform
# all the calculations at once on all the elements.

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
arr_totals = arr_prices * arr_quantities
print(arr_totals) # so much easier

# other examples:
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])
totals = units_feb + units_jan
print(totals)
# how much more or less did we sell in feb compared to jan?
print(units_jan - units_feb)
# Growth rate over the two monts
print(units_feb/units_jan)

# let me show you a restriction though
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80]) # only data for four products!
print(units_feb - units_jan) # ValueError. The two arrays don't have the same SHAPE:
print(units_jan.shape) # 5 elelments
print(units_feb.shape) # 4 elements
# need to have compatible shapes to sum, divide, subtract, or multiply
# this is why we cant add or remove from arrays: we need to know their shape at all times

# what else ca you do with arrays?

# we can compare them! 

units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])

feb_sold_more = units_feb > units_jan
print(feb_sold_more)
print(units_jan ** 2) 
print(np.sqrt(units_jan)) # the numpy library contains special versions of common math operations
# that are specifically designed to work with arrays

# error: we reported 10 fake transactions for each of the products in Jan:
print(units_jan - 10) # no error!

# there are many operations you can apply to arrays... and arrays also have methods that you can inspect
units_jan.mean() # You cna call the method mean() to know the mean value of an array... if the array
# has a numeric dtype
units_jan.std()

# we've already seen that you can index and slide arrays like lists:
prices = np.array([10, 5, 20, 30, 8])
print(prices[0:3]) # first three prices, first price, so on and so forth.
# When you index with a single value, you get a value of the dtype of the array
# when you slice an array, you get a new array

# when working with arrays, like with lists, you can edit the elements of the array:
# let's replace the first price by 15;
prices[0] = 15
print(prices)
# what if we want to now make the first two prices equal to 15 and seven?
prices[0:2] = [15,7]
print(prices) # arrays are still mutable! We just cannot change their shape

# everything that we've seen so far with indexing and slicing is 
# identical to what we do with lists

# we can do more powerful stuff with arrays!
my_mask = np.array([True, False, True, False, True])
prices = np.array([15, 7, 20, 30, 8])
print(prices[my_mask]) # I can index the prices using the mask: put the mask between square brackets
# after the array
# when you index with a mask, you are going to get in retunr only the values of the array
# where the corresponding position in the mask is true
# Think of overlaying the mask on top of the array: The True are the cutouts. Any value that is 
# in the cutout is going to be returned

# when are the masks useful?
quantities = np.array([5, 10, 15, -5, -7, 10]) # quantities cant be negative so lets remove them
# could we create a mask that would revela these errors?
my_mask = quantities < 0
print(my_mask) # Now we have the masK
# how can we use ti to spot all the erroneous values in quantities?
print(quantities[my_mask]) # we used the mask to see all the negative values in quantities and get them in an array
# now can we use the mask to replace all these negative values by 0?
quantities[my_mask] = 0 # you can use the mask to HIGHLIGHT all the negative values and assign the value zero to them
print(quantities)

quantities = np.array([5, 10, 15, 0, 0, 10]) # this is the number of customers a coffee shop has monday through sat
# 1. on average, how many customers did they see on the six days?
print(quantities.mean()) # 6.6667
# 2. on all the days they saw at least one customer, how many customers did they see?
my_mask = quantities >=1
one_q = quantities[my_mask]
print(one_q.mean()) # 10
# could have done it in one line
quantities[quantities >= 1].mean() # also 10

# final thing with array: fancy indexing... and thats pretty fancy
# lets say you have emails from four customers: 
emails = np.array(['quentin@colorado.edu', 'tony@yale.edu', 'jimmy@hbs.edu', 'goof@fah.edu'])
# how do we get the first email?
emails[0]
emails[0:2]
# with lists you can i index with a single value or (ii) to use a slice
# with arrays you can index with multiple values
# fancy indexing
print(emails[[0, 0, 1, 2, 0]]) # you give a LIST of values as an index
# double bracket

# why fancy? common example: select a random sample of rows in a dataset

# lets wrap up on arrays:
# 1. an array is a new type of iterable. It works a lot like lists
# 2. Excetpion 1: arrays only contain values of the same dtype
# 2. Exception 2: arrays only have a fixed shape. They cannot be popped appended or inserted
# 4. Thanks to these restrictions, arrays can be added to each other, subtracted from each other, etc etc
# these operations are performed on all elements of the array and are much faster
# 5. arrays can be compared, elelment-wise to create boolean arrays (masks)
# we can use masks to filter arrays and reassign values at specific positions
# 7. Arrays, like lists, can be indexed and sliced both to select and replace values
# 8. compared to lists, arrays accept two new forms of indexing: Boolean indexing (only two cvalues
# facing the true values in the mask returned), and fancy indexing (all the indexes specified in the list are returned).