# # 58. lesson - Variable scope
# # parts of code not interfering with other parts

# # Two types - global scope - global variable, loops and if
#             # local - functions


# # f1 - doesnt need parametres - they are optional

# # 1) here a is global
# # a = 100
# # a = 250 is global 
# a = 250
# def f1():
#     a = 100
# # 2) here it is local
#     print(a)
# print(f1())
# # functions create local scope inside - f2 cannot see 100
# # before a was global - 1)

# def f2():
#     a = 50
# # they both will work with the same variable a, but with diff. output
#     print(a)

# print(f2())
# print(a)

# # Output: 
# # 100
# # None
# # 50
# # None
# # 250

# # a = 250 is not overwritten even if it is redefined later as a = 100, a = 50 because it is global
# # Python does not allow us to change the global variable from inside the functions and creates a local variable a = 100
# # inside a function f1 and as well as for f2, global 250 was protected and printed out, local variable is removed from
# # memory after running, you can automatically use global variable but not to change it

# # if we had huge code with 50 functions, we wouldnt need to worry about writing new variables in
# # order not to overwrite an existing one by mistake
# # variable scopes must not overlap

# # you can use the global value as long as you do not change it (automatically)
a = 250
def f1():
    a = 100

    print(a)
print(f1())

def f2():
    a = 50

    print(a)

print(f2())
print(a)