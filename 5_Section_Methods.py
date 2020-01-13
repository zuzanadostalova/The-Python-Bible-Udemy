# # 24. lesson - String methods
# # string.method
# print("hello".count("e"))

# text = "Happy birthday"
# # text = "Happy birthday".count("a")
# print(text)
# print(text.count("day"))

# x = "Happy Birthday"
# # lower/upper - without changing the original string, strings are immutable data 
# # types = unchangable
# print(x.lower())
# print(x.upper())

# # to change it permanently - we need to assign x to upper case, overwriting
# x = x.upper()
# print(x)

# # to change it permanently - we need to assign x to lower case, overwriting
# x = x.lower()
# print(x)

# # Overwritten to the first capital letter
# # x = x.capitalize()
# # print(x)

# print(x.title())
# print(x)
# # Overwritten to both capital letters
# x = x.title()
# print(x)

# # How to find out which case is the word in?
# print(x.islower())
# # output: False
# print(x.isupper())
# # output: False
# print(x.istitle())
# # output: True
# # Is everything letters in the string? False, because there is a space
# print(x.isalpha())
# # output: False

# print("abcd".isalpha())
# # output: True

# print("123".isdigit())
# # output: True

# y = "happybirthday123"
# print(y.isalnum())
# # output: True

y = "happybirthday!123"
print(y.isalnum())
# output: False

# Index of a substring
x = "happy birthday"
print(x.index("birthday"))
# output: 6

# if the substring does not exist - substring not found error
# We use index as a hard stop

# Finding a substring - alternatively
print(x.find("birthday"))
# output: 6

# We use find when we do not want the program to crash even if the substring does not exist
print(x.find("jioshff"))
# output: -1; still valid index

# Both index and finding are case sensitive
# That is where .upper() or .lower() come at handy

# To strip a part of the code (Keep in mind that string is immutable!)
y = "0000happybday0000"
print(y.strip("0"))

# To strip the left part of the code
print(y.lstrip("0"))

# If you do not write anything in the parentheses, the strip strips spaces
name = input("What is your name? ")
print(name)
print(len(name))

# If you want to prevent inserting a space behind the name by accidentally hitting enter,
# you can use strip method
name = input("What is your name? ").strip()
print(name)
print(len(name))

# the rest in the documentation
