# 41. lesson - More ways to add items on the list
A = [5, 12, 72, 55, 89]
A = A + 1
# print(A)
# Output: error, can only concatenate list (not "str") to list

A = A + [1]
# I. add to A this list of one item = 1
print(A)
# I. Output: [5, 12, 72, 55, 89, 1]

A = A + "BCD"
# print(A)
# Output: error, can only concatenate list (not "str") to list

A = A + ["BCD"]
print(A)
# I. Output: [5, 12, 72, 55, 89, 1, 'BCD']

# or II. add list
A = A + list("BCD")
print(A)
# II. Output: [5, 12, 72, 55, 89, 1, 'BCD', 'B', 'C', 'D'] - added as separated elements

# not possible for integers - they are not iterable data type - cannot be converted to lists
A = A + list(123)
# print(A)
# Output: error, 'int' object is not iterable

A = [5, 12, 72, 55, 89]
A = A + [1,2,3]
print(A)
# Output: [5, 12, 72, 55, 89, 1, 2, 3]


# convert numbers into strings
A = A + list(str(123))
# no comas in between
print(A)
# Output: [5, 12, 72, 55, 89, '1', '2', '3']

A = [5, 12, 72, 55, 89]
A = A + [5, 6, 7, 8]
# added them separately
print(A)
# Output: [5, 12, 72, 55, 89, 5, 6, 7, 8]

A = A + [[5, 6, 7, 8]]
print(A)
# Output: [5, 12, 72, 55, 89, 5, 6, 7, 8, [5, 6, 7, 8]]

print(A[-1])
# Output: [5, 6, 7, 8]

A.append([10,11,12,13])
print(A)
print(A[-1])
# Output: [5, 12, 72, 55, 89, 5, 6, 7, 8, [5, 6, 7, 8], [10, 11, 12, 13]]

A = [5, 12, 72, 55, 89]
A = A.append(10)
print(A)
# Output: None, returns empty space, saved to A - deleted data, space from assignment

# If print(A.append()), the output is: append() takes exactly one argument (0 given)

print(type(A))
# Output: <class 'NoneType'> before it was list

print(type(A.append(10)))
# Output: 'NoneType' object has no attribute 'append'

A = [5, 12, 72, 55, 89]
A.insert(2,100)
print(A)
# inserting 100 at index 2

A = [5, 12, 72, 55, 89]
A.insert(2,[10, 20, 30])
print(A)
# the whole list at index 2

# if we would do A = A.insert(2,60) we would delete A -> lists are mutable after they are created

# s = "123"
# s[0] = 5
# Output: error - string is immutable

A = [1,2,3]
A[0] = 5
print(A)
# Output: [5, 2, 3]

A = A.append(5)
# A is now deleted
# type(A)...NonType

A = A.remove(2)
# A is now deleted
# type(A)...NonType