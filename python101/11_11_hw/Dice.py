import random

def unexpected(num_1, num_2):
    number = random.randint(num_1, num_2)
    print("It's a", number,"!")


def dice():
    ask = input("We are going to roll a dice. How many sides does it have? (number between 2 and 20) ")
    if 2 <= int(ask) <= 20:
        print("The dice is rolling!")
        unexpected( 1, int(ask))
    else:
        print("invalid number")
    

    


dice()