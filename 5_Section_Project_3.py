# # 26., 27., and 28. lesson - Project 3 - Email slicer
# # string = iterable data type - you can go step by step along it until you get to the end
# # each of these steps is called element and it has number that corresponds to its position
# # by using its index, you can get the element
# string="ABCDEF12345"

# # string is immutable iterable object - you can iterate over each element
# word = "supercalifragilisticexpialidocious"
# print(word[0])
# # s

# print(word[2])
# # p

# # slicing - variable[start:end:step]
# print(word[0:5])
# # output: super

# # We want every letter, in one element every time, so we put 1 - print(word[0:5:1])
# print(word[0:5:1])
# # output: super
# # or simply word[:5]

# # If we want every other letter, so we put 2 - print(word[0:5:2])
# print(word[0:5:2])
# # output: spr

# # How'd you get on?
# print(word[5:9:1])
# # output: cali

# # shortcuts - from a certain element till the end
# print(word[5:])
# # output: califragilisticexpialidocious

# # shortcuts - from a certain element till the end in steps of two
# print(word[5::2])
# # output: clfaiitcxildcos

# print(word[:7])
# # output: superca

# # How to reversed numbers of the indexes in the string?
# print(word[::-1])
# # goes from the end to the start
# # output: suoicodilaipxecitsiligarfilacrepus

# # we can count from the end - if we want "u"
# print(word[-2])
# # output: u

# print(word[-8])
# # output: i

# # we do not need to count, we can use the computer to do that
# print(word.index("cali"))
# # output: 5

# print(word.index("fragi"))
# # output: 9

# # we want to go from "cali" to "fragi"
# print(word[word.index("cali"):word.index("fragi")])
# # output: "cali"

# # we want to slice out "docious"
# print(word[word.index("docious"):])

# print(word[-7:])
# # output: docious

# # we want fragilistic
# print(word[word.index("fragilistic"):word.index("expia")])
# # output: fragilistic
# # note: the word index string needs to be at least 3 letters long

# print(word[9:20])
# # output: fragilistic

# print(word[-25:-14])
# output: fragilistic

# Coding challenge
word = "antidisestablishmentarianism"
answer = word[word.index("establishment"):word.index("ari")]
print(answer)


# Email slicer
# string formatting

# get user email address
email = input("What is your email address? ").strip()
print(len(email))

# slice out user name
name = email[email.index(""):email.index("@")]
print(name)

# or easily
user = email[:email.index("@")]
print(user)

# slice domain name without the country
domain = email[email.index("@") + 1 :email.index(".")]
print(domain)

# slice domain name
domain = email[email.index("@") + 1 :]
print(domain)

# format message
msg = "Your  user name is {}  and your domain name is {}"
output = msg.format(user, domain)
print(output)

# easier
output = "Your  user name is {}  and your domain name is {}".format(user, domain)
print(output)

# display the output msg

# 29. lesson - Section overview
# strings - made by '', "", """ """
# fix broken strings
# created hello world
# how to work with incompatible data types
# string methods - index, find, functions 
# slices
# quick quiz + coding challenge
# email slicer project
