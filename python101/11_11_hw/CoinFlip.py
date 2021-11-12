import random 


def coin_flip():
    ask = input("Would you like to flip a coin? ")
    if ask == "yes":
        print("You flipped a coin")
        coin = random.randint(0,1)
        if coin == 0:
            print("IT IS HEADS")
            ask = input("Would you like to flip a coin? ")
        else:
            print("IT IS TAILS")
            ask = input("Would you like to flip a coin? ")
    if ask == "no":
        print("coin not tossed")
           

coin_flip()