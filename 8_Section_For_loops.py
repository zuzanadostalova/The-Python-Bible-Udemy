# 50. lesson - For loops
# most useful loops
# "for" loops - variable (key) - changing on each cycle of the loop
# and iterable (students.keys()) - made up from elements
# In each cycle, the variable becomes the next value in the iterable
# operation on each value
# range function - set up number, create number iterables
# how to put "for" loops inside each other
# advanced process, powerful - lot of information in a one line of code

# Do not forget column (:) after end parentheses
# "for", variable = number, iterable = range (could be a list, string)
for number in range(1,1001):
    print(number)

for number in range(1,11,2):
    print (number)

# list
for list in [1,2,3,4]:
    print(list)

# string
for letter in "abcd":
    print(letter)

# If you wait, it tells you how to do it

# This is used:
vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))
# Output:There are 2 vowels.
       # There are 3 consonants.


# 51. lesson - "For" loops 2
students = {
    "male":["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for key in students.keys():
    print(key)
# Output: male, female = keys

for key in students.keys():
    print(students[key])
# Output:['Tom', 'Charlie', 'Harry', 'Frank']
# ['Sarah', 'Huda', 'Samantha', 'Emily', 'Elizabeth']

# To pull out each name
# "For" loop for following names
# students of the key male
# for every name in the male list - if there is a, print the name
# and subsequently female names
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
# Output:
# Charlie
# Harry
# Frank
# Sarah
# Huda
# Samantha
# Elizabeth

