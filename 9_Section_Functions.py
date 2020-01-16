# 56. lesson - Section overview
# learn how to create functions
# build a tic tac toe game

# 57. lesson - What are functions?
# x, y = parametres for the function to work
# This time I want sth from function - returns a value, but sth it needs to function but doesnt need
# to return anything
# def add(x,y):
#       x + y

def add(x,y):
       return x + y
    
print(add(5,10))

answer = add(100,20)
print(answer)

add(5,2)
answer = add(5,2)

# returning is not the same as print!
# print does not store variable, does not return anything

# a lot of function in two lines of code
word = "pen"
word[::-1]
def rev(text):
    return text[::-1]
print(rev([1,2,3,4,5]))
# print(rev("delirious"))

# be aware of EOF which appears e.g. when you forget to close parentheses!

# functions - reusable code, sometimes takes inputs and parametres, sometimes returns output
# stored in variable for later, function putting together two numbers
# print vs return - if I want to store for later
# functions working on any data type - rev variable

# Coding challenge:
def multiply(x,y):
    return x * y
answer = multiply(5,10)
print(answer)

