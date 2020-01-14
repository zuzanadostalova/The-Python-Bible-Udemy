# 43. lesson - What are dictionaries?
# symbol of squiggle brackets {}
# NameError: name 'Alice' is not defined...it is not a variable:
# error_students = {Alice:25, Bob:27}

# students = {}
students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}
print(students["Dan"])
# Output: 21
students["Fred"] = 25
print(students["Fred"])
# Output: 25...Fred was added to the dictionary

students["Alice"] = 26
print(students["Alice"])
# Alice's age was updated

# How to delete Fred? 
del students["Fred"]
# Going to delete the item with the key of Fred along with any assoc. values

# print(students["Fred"])
# Output: KeyError: 'Fred'

print(students.keys())
# Output: dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma'])...iterable but not iterable
# print(students.keys()[0])
# Output: 'dict_keys' object is not subscriptable... we need to turn it into a list
a = list(students.keys())
print(a)
print(a[0])
print(a[1])
print(a[2])
print(students.values())

list(students.values())[2:]
# We cannot take slices 
# print(students.values()[2:])
# Output: 'dict_values' object is not subscriptable

# print(students.values()[0])
# Output: 'dict_values' object does not support indexing

# In dictionaries, items do not have an order, we access them through a key
print(students)
# the order in the output is not important - just the keys and values are matched

print(students["Dan"])
# Output: 21

# print(students[0])
# Output: KeyError: 0

# first you look up a key and you get a value
# key = students name, value = age

print(students.items())
# Output: dict_items([('Alice', 26), ('Bob', 27), ('Claire', 17), ('Dan', 21), ('Emma', 22)])
# Tuples
