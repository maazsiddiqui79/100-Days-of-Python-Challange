print("-------------------Welcome to Treasure Island. Your mission is to find the treasure-------------------")
print("\t\t\t\tYour mission is to find the treasure.")
print("You're at Seashore. Where do you want to go? ['left','right']")
lr_input= input("Where do you want to go?\n").lower()

if lr_input=="Right".lower():
    print("Fall into a hole.Game Over.")
elif lr_input == "left".lower():
    print("You've come to a lake.\n There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat ,\nor 'swim' to swim across")
    ws_input= input("Where do you want to go?\n").lower()
    if ws_input == "swim":
        print("You get attacked by an angry Shark.\n Game Over.")
    elif ws_input == "wait":
        print("You arrive at the island safely.\n There is a house with 3 doors.")
        print("One Red ,One Yellow,One blue.\n")
        door = input("Choose any Door\n").lower()
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("You Win!\nyou find the treasure \nGame End.")
        else:
         print("You Entered a wrong input... ,You are disqualified")
        
    else:
        print("You Entered a wrong input... ,You are disqualified")
        
    









else:
    print("You Entered a wrong input... ,You are disqualified")
    exit()
