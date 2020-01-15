# 49. lesson - Baby conversation simulator

# # My solution:
# while True:
#     answer = input("Why is the sky blue? ").strip().lower()
#     if answer == "just because":
#         break

# PB:
# answer = input("Why is the sky blue? ").strip().lower()

# while answer != "just because":
#     answer = input("why? ").strip().lower()

# list of questions
# random function
from random import choice

questions = ["How come that birds fly?: ", "Why is sun shining?: ",
"Why do dogs have four legs?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why? ").strip().lower()

print("Oh...okay.")


        
    
    
