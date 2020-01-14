# 45. lesson - Cinema simulator
films = {
    "Finding Dory":[3.5],
    "Bourne":[18.5],
    "Tarzan":[15.5],
    "Ghost busters":[12.5]
}

# print(films["Finding Dory"])

while True:
    answer = input("Hello. What movie would you like to see? (Finding Dory, Bourne, Tarzan, or Ghost busters) ").strip().title()
    if answer == "Finding Dory":
        age = input("What is your age? ")  

        if int(age) >= 3.5:
            input("How many tickets would you like to buy? ")

        else:
            print("I am sorry, you cannot buy any ticket.")


    elif answer == "Bourne":
        age = input("What is your age? ")
        
        if int(age) >= 18.5:
            input("How many tickets would you like to buy? ")

        else:
            print("I am sorry, you cannot buy any ticket.")


    elif answer == "Tarzan":
        age = input("What is your age? ")

        if int(age) >= 15.5:
            input("How many tickets would you like to buy? ")

        else:
            print("I am sorry, you cannot buy any ticket.")
            

    elif answer == "Ghost busters":
        age = input("What is your age? ")

        if int(age) >= 12.5:
            input("How many tickets would you like to buy? ")

        else:
            print("I am sorry, you cannot buy any ticket.")

