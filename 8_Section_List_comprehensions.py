# 52. lesson - List comprehensions
# Shortcut method - variables + "for" loops + "if" statements to comprehend a list in 
# one line of code
# variable x, stored in the list, x loops through...1, 2, 3...100, we keep x if divisible by 2
# 
even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(1,101) if x % 2 != 0]
print(odd_numbers)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# list of lists, 
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)