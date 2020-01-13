# 36. lesson - overview of the 7. Section - Python datastructures
# datastructures - to group data together and store them under one variable name -> to operate
# thousands/milions of data in a single line of code

# Lists, Tuples, and Dictionaries
# Build Travis - security system
# Cinema booking simulator - age ratings

# 37. lesson - Lists
our_list = [27, 46, -5, 17, 99]
print(our_list)

# combination of data types
jackson = ["A", "B", "C", 1, 2, 3, "Do", "Re","Mi", True, False]
print(jackson)

# list is an iterable data type
# we can get any item ->

print(jackson[4])
# Output: 2

print(jackson[-2])
# Output: True

x = jackson[6]
print(x)

# jackson[start:end:step]

# A, B, C
print(jackson[0:3])

# this does not change the original data

our_list = [1, 2, [3, 4, 5], 6, 7, 8]
print(our_list)
# the whole list inside is index 2

# for the contents of the sublist:
print(our_list[2][0])
# Output: 3

# for the contents of the sublist:
print(our_list[2][1:])
# Output: [4, 5]

# for the contents of the sublist:
print(our_list[2][0::2])
# Output: [3, 5]

# functions for two variables with the same name "our_list"

