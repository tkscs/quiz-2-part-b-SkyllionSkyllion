def forest():
    response = input("You are currently in the forest. Would you like to go north (n) or go east (e)")
    if response == "n":
        print("You find a cave with treasure! You win!")
    elif response == "e":
        print("You find a river")
        river()
    else:
        print("please input a valid response")
        forest()

def river():
    response = input("You are currently at the river. Would you like to go back to the forest (b), or swim across the river (s)")
    if response == "b":
        print("You go back to the forest")
        forest()
    elif response == "s":
        print("You swim in the river and die :C")
    else:
        print("Please input a valid response")
        river()


forest()