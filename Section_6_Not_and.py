# 33. Not + end
# What logical operators? They differ from comparison operators
# Log. operators combine and modify conditions into bigger ones

# "Not" operator
print(not True)
# Output: False

print(not False)
# Output: True

print(not 2 < 3)
# Output: False

print(not 4 == 3)
# Output: True

x = 10
y = 20
if not y < x:
    print("It worked!")

# A=0 then output=1
# A=1 then output=0

# "And" operator
# two inputs - True only if both inputs are True
# A=0, B=0, output=0
# A=0, B=1, output=0
# A=1, B=0, output=0
# A=1, B=1, output=1