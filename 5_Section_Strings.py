# 19. lesson - Section overview
# for data analysis - pandas, NumPy, SciPy

# 20., 21., 22., and 23. lesson - Hello world
print("hello")
name = "Ziyad"
print(type(name))

# message = "John said "See you later""
# how to correct this faulty string? ->
message = 'John said "See you later"'

# How to fit a long text into one variable? Triple quotes either ''' or """
# punctuation inside does not matter - there can be a double quote etc 
romeo = """Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventured piteous overthrows
Do with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, nought could remove,
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend."""
print(romeo)

# Hello world
hello = "Hello world!"
print(hello)

# gathering input, combine various typr of data to make meaningful messages, to create a program
# taking user input, processing it, and giving an output



# The second project - Hello World
# First - write an outline - comments

# Ask user for name
name = input("What is your name? ")

# Ask the user for their age
age = input("How old are you? ")

# Ask user for the city where they live
city = input("What city do you live in? ")

# Ask user what they enjoy
love = input("What do you love doing? ")

# # Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)
print(output)

# Print output

# open Python doc - Py standard library - we do not have to write the import function - all the
# functions are built-in
# Look up input function - the doc tells you how to use it

# Prompt is optional
s = input("Monthy Python's Flying Circus")


# Every input statement in Python is gonna be 

# learn how to concanate strings
A = "part one"
B = "part two"

print(A + B)
print(A*3)
print("=" * 20)
print("TITLE")

# repetition - saves time

# We cannot combine string and integer - we need int() function to put them together
A = "part one"
B = 1
print(A + str(B))
# output = part one1

# Formatting through placeholders - {}
print("{} - {}".format(A,B))
# output = part one - 1

print("{} - {}".format(B,A))
# output = 1 - part one, but not a really elegant solution

print("{1} - {0}".format(A,B))
# output = 1 - part one, better solution for the previous case


# The coding challenge I
start = "I am "
age = 24
end = " years old"

string = "{}{}{}."
output = string.format(start, age, end)
print(output)

# The coding challenge II
name = "Zuzana"
age = 24
place = "Brno"
love = "guitar"
string = "Hello my name is {} and I am {} years old. I live in {} and I love {}."
output = string.format(name, age, place, love)
print(output)
