# 60. lesson - 9 Section Key arguments default parametres

def about(name, age, likes): # parameters - age...
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence # saving

print(about("Jack",23,"Python")) # to call the function, positional arguments
# Output: Meet Jack! They are 23 years old and they like Python.

# arguments - Jack, 23, Python
# arguments Jack matches parameter name when in correct order or:
about(age = 23, name = "Jack", likes = "Python")
# each arg associated with a key word matching the parameter
# more flexible than positional arguments

# when we do not wish to put on a value or we do not know
# we have to set the unknown value a default value

def about(name = "Ziyad", age = 23, likes = "Python"): # parameters with default values have to go the last
    sentence = "Meet {}! He is {} years old and he likes {}.".format(name, age, likes)
    return sentence

print(about("Jack", 23))
print(about("Jack", 23, "Football"))
print(about()) # uses defaults - we can leave out arguments,
# of not, uses "JAck" in this case
# Output: Meet Jack! They are 23 years old and they like Football. - overwrites a default