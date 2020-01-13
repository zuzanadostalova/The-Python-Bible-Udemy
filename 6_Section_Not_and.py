# # 33. Not + end
# # What logical operators? They differ from comparison operators
# # Log. operators combine and modify conditions into bigger ones

# # "Not" operator
# print(not True)
# # Output: False

# print(not False)
# # Output: True

# print(not 2 < 3)
# # Output: False

# print(not 4 == 3)
# # Output: True

# x = 10
# y = 20
# if not y < x:
#     print("It worked!")

# # A=0 then output=1
# # A=1 then output=0

# # "And" operator
# # two inputs - True only if both inputs are True
# # A=0, B=0, output=0
# # A=0, B=1, output=0
# # A=1, B=0, output=0
# # A=1, B=1, output=1

# C = 10
# D = 5
# if C > 10 and D > 1:
#     print("It worked!")
# # No output because False and True

# print(False and True)
# # Output: False

C = 10
D = 5
if C >= 10 and D > 1:
    print("It worked!")
# Output: It worked! because C equals to 10

# Combination of "Not" + "And"
if not (C > 10 and D > 1):
    print("It worked!")
# Whatever is inside the brackets is going to be executed first
# Inside the brackets: C > 10 is False, D > 1 is True; the content of the brackets is False
# Outside the brackets: What is not False? True; the code will run

# This way we can allow the operations to happen on each other - without the brackets we 
# would just take the not of C

