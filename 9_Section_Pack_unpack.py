# 61. lesson - Packing and unpacking
print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)
# Output: 
# 1 2 3 4 5
# [1, 2, 3, 4, 5]
# 1 2 3 4 5

# unpacking - each item from iterable data type (list) and each becomes its own argument
# creating mini arguments

print("abc")
print(*"abc")
print("a","b", "c")
# Output: 
# abc
# a b c
# a b c

# def add(x,y):
#     return x + y

# print(add(10,10))
# Output: 20

# def add(*numbers): # tuple called numbers, unpacking for normal arguments
#     total = 0
#     for number in numbers:
#         total = total + number
#     return(total)

# print(add(1,2,3,4,5,6,7,8,9))
# Output: 45, all arguments in tuple numbers ... numbers = (1,2,3,4,5,6,7,8,9)
# overturn back the value
# packing useful when we do not know how many arg. we are expecting
# loop through as big tuple as we want - flexibility

# add(y = 1, x = 2) # positional argument

def about(name, age, likes):
        sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
        return sentence

dictionary = {"name": "Ziyad", "age":23, "likes":"Python"} # even if we switch the order of the
# key words
print(about(**dictionary)) # Unpacking - key word arguments 

# or print(about(name: "Ziyad", age:23, likes:"Python")) but we do not need to do 
# it manually - automat. gen. data and pack them all in once

def foo(**kwargs): # kwargs are numbers
        for key, value in kwargs.items():
                    print("{}:{}".format(key, value))

print(foo(huda = "Female", ziyad = "Male")) # we can assign to either female of male as many
# key words as we want

# Output:
# huda:Female
# ziyad:Male

# * to pack and unpack iterables - to pack them into tuples, or unpack them as argument
# putting them into function - e.g. add function any amount of numbers
# only value - 1 piece of info

# ** key word argument - unpack into dictionary inside of yout function or pack them into
# a dict for your function - 2 piece of info 
 