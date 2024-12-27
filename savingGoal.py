budget = float(input("type in your budget"))
bleh = 0
expense = 0
def remaining():
    global budget
    global expense
    budget  = budget - expense
    expense = 0
    return budget
def ram():
    global budget
    global bleh
    budget = budget - bleh
    bleh = 0
    return budget
print("e is to enter expense,c is to check budjet,s is to set saving goal, r is to check if purchase is expensive")
print("n is to check how close you are to goal,v is to close")
while True:
    question = input("what operation do you want to carry out").capitalize()
    if question == "E":
        expense= float(input("how much are you collecting"))
        if expense > budget:
            print("Try again amount is too high")
        else:
            print(f"{expense} has been deducted")
            remaining()
    if question  == "C":
        print(remaining())
    if question == "S":
        save = float(input("enter a savings goal"))
    if question == "R":
        bleh = float(input("how much are you taking"))
        if budget/bleh < 1.5:
            print("purchase is too expensive and can ruin budget")
            if bleh > budget:
                print("amount too high")
            else:
                ram()
        else:
            ram()
            print(f"{bleh} has been deducted")
            
    if question == "N":
        close = (budget/save)*100
        if close < 100:
            print(f"you are {close}% to your saving goal")
        if close == 100:
            print("you have saved up to your goal")
        if close > 100:
            print("you have surpassed your goal")
    if question == "V":
        print("Thank you for using the app")
        break


