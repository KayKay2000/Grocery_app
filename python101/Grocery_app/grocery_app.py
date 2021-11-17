
shopping_list= {'Fiesta':
                    ['milk','soda','fish'], 
                'Walmart': 
                    ['paper', 'napkins', 'plate', 'chips'], 
                'Sams Club':
                    ['chicken', 'beef', 'eggs', 'sugar', 'salt', 'pepper', 'honey']}


def grocery_app():
    
    mainmenu = input(""" 
    1. Create shopping list
    2. Select shopping list
    3. Delete shopping list
    4. View all shopping list
    5. Quit app

    Select number of the action you want to take.  """)
    # while True:
    if mainmenu == "1":
        store_name = input("Name of new shopping list: ")
        item = input(f"What item would you like to add to shopping list {store_name} ")
        shopping_list[store_name]= item
        print(shopping_list)
    elif mainmenu == "2":
        for key, value in shopping_list.items():
            # item_string= ""
            # for item in value:
            #     item_string = item_string + item + "," 
            print(key)
        list_name = input("Which list would you like to edit? ")
            
                
        

    elif mainmenu == "3":
        for key, value in shopping_list.items():
                print(key)
            delete= input("Which list would you like to delete? ")
            if delete == value:
                del shopping_list[value]
    elif mainmenu == "4": 
        for key, value in shopping_list.items():
            item_string= ""
            for item in value:
                item_string = item_string + item + "," 
            print(f"{key}: {item_string}")
        # elif mainmenu == "5":
        #     print("Quitting app..")
        #     break  
        # write an else statement to say they made an invalid choice 
grocery_app()