# # 32. lesson - If statements
# if True:
#     print("It worked!")
# # Output: It worked!

# if False:
#     print("It worked!")
# # No output

# num1 = 100
# num2 = 50

# if num1 > num2:
#     print("Num1 is bigger than num2")
# # Output: Num1 is bigger than num2

# if num1 < num2:
#     print("Num1 is bigger than num2")
# # No output

# if num1 > num2:
#     print("Num1 is bigger than num2")
# else:
#     print("Num2 is bigger than num1")


num1 = 160
num2 = 150
if num1 > num2:
    print("Num1 is bigger than num2")
elif num2 > num1:
    print("Num2 is bigger than num1")
else:
    print("Both numbers are equal")
# play with num1, num2 values to get each time different output

# review - running only if True
if condition:
    code
elif condition2
    code2
elif condition3
    code3
else:
    code4