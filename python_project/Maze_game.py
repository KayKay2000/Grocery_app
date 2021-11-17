from datetime import date
today = date.today()
now = today.strftime("%B %d, %Y")

def intro():
    print(f"""
    It's a chilly day on {now}. 
    Your best friends think it's a good idea to go to a maze today.
    They found a new maze online and want to go check it out. 
    They ask you if you want to go too...  """)
    while True:
        main_menu =input("""
        A. You choose to stay home and catch up on your coding homework
        B. You want to go see the new maze! """) 
        if main_menu== "A" or main_menu == "a":
            print("""
            You tell your friends that you need to study and wave goodbye. 
            The next day you learn about a tragic accident that occurred at a new maze.
            You hope your friends are okay...""")
            Try_again = input("Would you like to try again? yes or no ")
            if Try_again == "yes" or Try_again == "Yes":
                main_menu
            if Try_again =="no" or Try_again == "No":
                print("You'll be back")
                break
        if main_menu == "B" or "b":
            print("""
            You put on your jacket and head out with your friends.
            Once you get there, you and your group of friends have a choice of three items:
            rock, sword, shield, emerald, stick, torch """)
            options= "rock, sword, shield, emerald, stick, torch"
            items_list= ""
            item1= input("What is the first item you choose? ")
            if item1 in options:
                print(f"You chose {item1}")
            else:
                print("Input invalid, try again. ")
                item1 = input("What is the first item you choose? ")
            items_list += item1 + ", "
            item2  = input("What is the second item you choose? ")
            if item2 in options and item2 not in items_list:
                print(f"You chose {item2}")
            else:
                print("Input invalid, try again")
                item2 = input("What is the second item you choose? ")
            items_list += item2 + ", "
            item3 = input("What is the third item you choose? ")
            if item3 in options and item3 not in items_list:
                print(f"You chose {item3}")
            else:
                print("Input invalid, try again")
                item3 = input("What is the third item you choose? ")
            items_list+= item3 
            print(f"You chose these items: {items_list}. Time to enter the maze!")
        
    

intro()
