# # 47. lesson - section overview
# # While loop
# # baby conversation simulator
# # for loops and list comprehensions
# # pig-latin translator

# # 48. lesson - While loop
# # repeating codes over again
# # while condition
#     # code

# # runs forever
# while True:
#     print("Hello")

# # always True...runs forever
# while 2>1:
#     print("Hello")

# # does not run
# while False:
#     print("Hello")

# print numbers from 1-10
# print(1), print(2)...

# number = 1

# while number <=10:
# # less or equals to ten - 1-10
#     print(number)
# # event. 10 + 1 = 11 - does not comply with the first condition
#     number = number + 1
# # Output: 
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10

# while number <=1500:
#     print(number)
#     number = number + 1
# # 1...1500

# combination of loops with "if"
number = 1
while number <= 1500:
    if number % 2 == 0: 
# print numbers divisible by 2 - even
        print(number)
    number = number + 1
# Output:
# 1490
# 1492
# 1494
# 1496
# 1498
# 1500

number = 1
while number <= 1500:
    if number % 2 != 0: 
# print odd numbers - when remainder does not equal 0
        print(number)
    number = number + 1
# Output: 
# 1491
# 1493
# 1495
# 1497
# 1499

L = []

while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)
print("Sorry, list is full")
print(L)
# Output: 
# Please add a new name: Z
# Please add a new name: B
# Please add a new name: C
# Sorry, list is full
# ['Z', 'B', 'C']