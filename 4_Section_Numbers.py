# Section 4: Numbers in Python
# 12. lesson - Overview of the section Numbers
# comp will do math for you, learn how to control the order of the computations,
# learn about floats

# make a health potion for a video game character
# use numbers to create difficulty system
# learn about using External Python modules

# 13. lesson - Basic Arithmetic, Floats, and Modulo
# Basic mathematical operations, Modulo function, the float variable type,
# Learn the difference between Python 2 and 3
# mathematical operator - symbol performing mathematical operations 
# Python 2 - division gives an integer input whereas Py3 gives a float (fixed many problems)
# type(0.5) 
# <class "float"> - higher precision with float taking more memory

# Modulo - %, shift 5 on Windows, shift = Mac
# 5 % 3; the output is 2 ... 5 / 3 = three will go to five once with remainder of two 
# 10 % 2 the output is 0 ... 10 / 2 = two will go to two twice with remainder of zero

# 14. lesson - Ordering Operations
# BODMAS - ordering system, closer to B - higher priority
# Brackets () - executed first
# Order - raising number to power of something else
# Division
# Multiplication
# Addition
# Subtraction

# the correct example: 2 * (5-1) = 8

# 15. and 16. lesson - Crafting a health potion
# represent health in simple manner - as a number

# import random
# health = 50

# # easy, for middle 2, difficult 3
# difficulty = 3

# # potion_health = random.randint(25,50) 
# # print(potion_health)

# # to employ difficulty

# potion_health = int(random.randint(25,50) / difficulty)
# all_health = potion_health + health
# print(all_health)

# 17. lesson - Python math module
# rounding numbers to the nearest integer
round(1.5)
print(round(1.5))

# import math module
import math

# force round down - to the floor
math.floor(1.5)
print(math.floor(1.5))

# force round up - up to the ceiling
math.ceil(2.1)
print(math.ceil(2.1))

# pi = 3.141592653589793
math.pi
print(math.pi)

# exponential = 2.718281828459045
math.e
print(math.e)

# build-in trigonometrical functions - radians
math.sin(math.pi/2)
print(math.sin(math.pi/2))

math.sin(math.pi)
print(math.sin(math.pi))

math.floor(math.sin(math.pi))
print(math.floor(math.sin(math.pi)))

math.cos(0)
print(math.cos(0))

math.asin(0)
print(math.asin(0))

math.acos(0)
print(math.acos(0))

# Output is 5.0; Square 3 = 9, square 4 = 16, 16 + 9 = 25, square root of 25 is 5
math.hypot(3,4)
print(math.hypot(3,4))

# Output is 8.0; 2 to the power of 3
math.pow(2,3)
print(math.pow(2,3))

# Also build-in operations 2**3 gives the output 8 but in this case it is integer

# 9 to the power of 2
math.pow(9,2)
print(math.pow(9,2))

# e to the power of 2
math.exp(2)
print(math.exp(2))

# natural log of exponential = 1
math.log(math.e)
print(math.log(math.e))

# based 10 log
math.log10(1000)
print(math.log10(1000))

math.log2(8)
print(math.log2(8))

# knowledge test

# coding challenge - calculations, assigning variables
