# 45. lesson - Cinema simulator
# the first item in the list - age, the second one - number of tickets
films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost busters":[12,5]
}

# # print(films["Finding Dory"])

# # My way
# while True:
#     answer = input("Hello. What movie would you like to see? (Finding Dory, Bourne, Tarzan, or Ghost Busters) ").strip().title()
#     if answer == "Finding Dory":
#         age = input("What is your age? ")  
#         if float(age) >= 3:
#             requested_tickets = input("How many tickets would you like to buy? ")
#             tickets = 3
#             if tickets >= int(requested_tickets):
#                 print("Thank you for your purchase. Your tickets are on the way.")
            
#             else:
#                 print("I am sorry, there are not enough tickets left.")

#         else:
#             print("I am sorry, you are not old enough to watch this movie.")

#     # When doing changes, do not forget to go out of the loop and back into the zsh shell!


#     elif answer == "Bourne":
#         age = input("What is your age? ")
        
#         if float(age) >= 18:
#             requested_tickets = input("How many tickets would you like to buy? ")
#             tickets = 20
#             if tickets >= int(requested_tickets):
#                 print("Thank you for your purchase. Your tickets are on the way.")
            
#             else:
#                 print("I am sorry, there are not enough tickets left.")


#         else:
#             print("I am sorry, you are not old enough to watch this movie.")


#     elif answer == "Tarzan":
#         age = input("What is your age? ")

#         if float(age) >= 15:
#             requested_tickets = input("How many tickets would you like to buy? ")
#             tickets = 200
#             if tickets >= int(requested_tickets):
#                 print("Thank you for your purchase. Your tickets are on the way.")
            
#             else:
#                 print("I am sorry, there are not enough tickets left.")

#         else:
#             print("I am sorry, you are not old enough to watch this movie.")


#     elif answer == "Ghost Busters":
#         age = input("What is your age? ")

#         if float(age) >= 12:
#             requested_tickets = input("How many tickets would you like to buy? ")
#             tickets = 10
#             if tickets >= int(requested_tickets):
#                 print("Thank you for your purchase. Your tickets are on the way.")
            
#             else:
#                 print("I am sorry, there are not enough tickets left.")

#         else:
#             print("I am sorry, you are not old enough to watch this movie.")

# Tutorials way:
while True:

    choice = input("Hello. What movie would you like to see? ").strip().title()

    if choice in films:
        age = int(input("What is your age? ").strip())  

        if age >= films[choice][0]:
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film.")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
            
        else:
            print("You are too young to watch movie.")
    else:
        print("We do not have that movie...")



