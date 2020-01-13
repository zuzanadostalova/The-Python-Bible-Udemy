# 38. lesson - Travis the ridiculou security system
# Project 4

# I. remove data from a list
known_users = ["Ada", "Berthold", "Clementine", "Dominic", "Emmett", "Fin", "Geralt", "Hugh"]

# How many users?
print(len(known_users))

# To create a while loop
while True:
    print("Hello! My name is Travis.")
# Ask for a name + strip a possible accidental space
    name = input("What is your name? ").strip().capitalize()

# name = input(("What is your name? ").strip()).capitalize() would work, however, the strip would
# remove space behind the question mark
# capitalize directly after strip; for the change to take place it is necessary to close the loop
# within 1:Python terminal, and to open it again in zsh

    if name in known_users:
       print("Name recognised.")
    else:
        print("Name NOT recognised.")
# Hello! My name is Travis.
# What is your  name? looped

# Is this name in the list?
# "in" key word
L = [1, 5, 2, 6, 2, 9]
print(2 in L)
# Output: True

print(10 in L)
# Output: False

# 39. lesson - Travis
# String formatting

known_users = ["Ada", "Berthold", "Clementine", "Dominic", "Emmett", "Fin", "Geralt", "Hugh"]

while True:
    print("Hello! My name is Travis.")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello, {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)? ").lower()

# if remove == "y" or remove == "Y": or easily input().lower() and if remove == y - only lowercase!
        if remove == "y":
            known_users.remove(name)
            print(known_users)

# removed permanently - in the next loop removed still
# ['Ada', 'Berthold', 'Clementine', 'Dominic', 'Emmett', 'Fin', 'Geralt', 'Hugh']
# ['Berthold', 'Clementine', 'Dominic', 'Emmett', 'Fin', 'Geralt', 'Hugh']

    else:
        print("Name NOT recognised.")

# print("Hello, " + name)
# or print("Hello {}!".format(name))

# In case I know just the index and not specifically what I want to
L = [1, 2, 3, 4, 5]
del L[0]
print(L)

example = ["A", "B", "C", "A", "B"]
example.remove("A")
print(example)
# Output: ['B', 'C', 'A', 'B'] - only the first "A" is removed

# Solution to remove only the second A:
example = ["A", "B", "C", "A", "B"]
del example[3]
print(example)
# Output: ['A', 'B', 'C', 'B']

# .remove and del provide flexibility in removal of contents of a list  

# we can delete slices using the "del" key
del example[0:2]
print(example)
# Output: ['C', 'B']

# 40. lesson - Travis