# 34. lesson - Or

# "Or" operator
# two inputs - True only if either one or both are True
# A=0, B=0, output=0
# A=0, B=1, output=1
# A=1, B=0, output=1
# A=1, B=1, output=1

C = 5
D = -1
if C > 1 or D > 1: 
    print("It worked!")
# Output: It worked!
# A=1, B=0, output=1
print(True or False)

C = 5
D = 5
if C > 1 or D > 1: 
    print("It worked!")
# Output: It worked!
# A=1, B=1, output=1

if C > 100 or D > 100: 
    print("It worked!")
# No output
# A=0, B=0, output=0
print(False or False)

if not (C > 100 or D > 100): 
    print("It worked!")
# Output: It worked!
# A=0, B=0, output=1 because outside the brackets not
