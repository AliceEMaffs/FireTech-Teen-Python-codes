# Magic Ball game
# Shake the ball and ask a qu
# Your fate will be given!
# Displays one of 20 random answers
from random import seed
from random import randint

fate == True
#Ask user if they dare know their fate
daretoknow = str(input("Would you like to play the Magic Ball Game?"))
if daretoknow == "y":
    fate == True
    while fate == True:
        #Input the question here
        qu = str(input("What would you like to know? Type exit to leave"))
        if qu == "exit":
            fate == False
        else:
            continue
        for i in range(0,6):
            #Random number generator
            seed(1) # seed random number generator
            n = randint(0,6) # generate some integers
            print(n)
            if n == 1:
                print("Certainly")
            elif n == 2:
                print("Maybe, I'm not sure right now..")
            elif n == 3:
                print("Absolutely not!")
            elif n == 4:
                print("If you really hope so, maybe it will?")
            elif n == 5:
                print("Try again later..")
            else:
                print("I don't know")
else:
    fate == False    
