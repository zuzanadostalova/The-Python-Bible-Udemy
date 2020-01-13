# # 34. lesson - "Or" operator

# # "Or" operator
# # two inputs - True only if either one or both are True
# # A=0, B=0, output=0
# # A=0, B=1, output=1
# # A=1, B=0, output=1
# # A=1, B=1, output=1

# C = 5
# D = -1
# if C > 1 or D > 1: 
#     print("It worked!")
# # Output: It worked!
# # A=1, B=0, output=1
# print(True or False)

# C = 5
# D = 5
# if C > 1 or D > 1: 
#     print("It worked!")
# # Output: It worked!
# # A=1, B=1, output=1

# if C > 100 or D > 100: 
#     print("It worked!")
# # No output
# # A=0, B=0, output=0
# print(False or False)

# if not (C > 100 or D > 100): 
#     print("It worked!")
# # Output: It worked!
# # A=0, B=0, output=1 because outside the brackets not
# # What is not False? True

C = 6
D = 2
if (C > 5 and D > 5) or (C > 1 and D > 1):
    print("It worked!")
# C > 5 ... True, D > 5 ... False, the whole bracket is False
# C > 1 ... True, D > 1 ... True, the whole bracket is True

print(False or True)

C = 6
D = 2
if not ((C > 5 and D > 5) or (C > 1 and D > 1)):
    print("It worked!")

# Quiz:
# (True or False) and (False or True) is...True
# first solve each of the brackets; if at least one inside the brackets is True, then the bracket 
# is True because of its "or" operator
# both brackets are True, therefore the output of the brackets + "and" is True

# vs.
# (True and False) or (not True and True) is...False
# The first bracket is False - "and" is True only if both of the inputs are True
# The second brackets is False as well - not True = False, False and True is False
# False or False is False

# 35. lesson - overview of the 6. Section - Logic and conditional flow
