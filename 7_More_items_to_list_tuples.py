# # 41. lesson - Tuples
# # similarly used as lists
# # data type vs. list (list can be changed) - tuple cannot be changed once 
# # created - immutable (as well as strings)

our_tuple = 1,2,3,"A","B","C"
# # better to write in this way
# our_tuple = (1,2,3,"A","B","C")
# print(type(our_tuple))
# # Output: <class 'tuple'>

# # tuples are iterable - we can pick each element or slices of elements as lists and strings
# # using element index

# print(our_tuple[0:3])
# # Output: (1, 2, 3)

# our_list = [1,2,3,4,5,6,7]
# our_list[2] = 100
# print(our_list)
# # Output: [1, 2, 100, 4, 5, 6, 7]

# our_tuple = 1,2,3,"A","B","C"
# our_tuple[2] = 100
# print(our_tuple)
# # Output: 'tuple' object does not support item assignment  - it is immutable
# we use tuple as a secure way how to store protected data for later

# # tuple() - turns other data type into tuple
# A = [1,2,3]
# print(tuple(A))
# # Output: (1, 2, 3), A stays the same
# print(A)
# # Output: [1, 2, 3]


# # permanently by reassignment:
# A = tuple(A)
# print(A)
# # Output: (1, 2, 3), A changed into tuple


# s = "1,2,3,4,5,6,7"
# s[2] = "a"
# # Output: 'str' object does not support item assignment  - it is immutable

# Tuples - multiple assignment
(A, B, C) = 1, 2, 3
print(A)
print(B)
print(C)
# Output: 1
#         2
#         3

# Lists - multiple assignment
D, E, F = [1,2,3]
print(D)
print(E)
print(F)
# Output: 1
#         2
#         3

# Strings - multiple assignment
G,H,I = "789"
print(G)
print(H)
print(I)
# Output: 7
#         8
#         9

# tuples: to protect valuable data, through tuple function or by separating few values with 
# comas, surround tuple def with parentheses

# how to do multiple assignments with tuples, lists, and strings
