# 38. lesson - Travis the ridiculou security system
# Project 4

# I. remove data from a list
known_users = ["Ada", "Bertold", "Clementine", "Dominic", "Emmett", "Fin", "Geralt", "Hugh" ]

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
# # "in" key word
# L = [1, 5, 2, 6, 2, 9]
# print(2 in L)
# # Output: True

# print(10 in L)
# # Output: False

# 39. lesson - Travis
