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