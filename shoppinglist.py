# While loops

while True:
    print("Please choose an option:")
    print("A: Chess!")
    print("B: Tic Tac Toe!")
    print("C: Nuclear war!")
    print("X: To exit menu")

    userchoice=input("Pick an option now: ")
    if userchoice.upper() == "A":
        print("Chess.")
    elif userchoice.upper() == "B":
        print("Tic tac to")
    elif userchoice.upper() == "C":
        print("Boom you lost!")
    elif userchoice.upper() == "X":
        print("Byeeee!")
        break
    else:
        print("That was not a valid option!")

print("Left the loop exiting now!")
