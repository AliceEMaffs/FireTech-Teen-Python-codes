# Day 3 Challenges
# Rock paper sissors game

player1name = input("Enter the name of playyer on:\n")
player1name = input("Enter the name of player 2:\n")

#list for games won and lost
player1 = []
player2 = []

# Have a random generator that picks one of the three
rpslist = ["rock","paper","sissors"]

pick = input("Would you like to play random or manually")
if pick == "
def rockpapersissorschoose()
    print("You are playing manually:\n")
    print("Pick one of the following:\n")
    print("(a) Rock, (b) Paper, (c) Sissors")
    choice = input()

    if choice.lower() == "a":
        Rock()
    elif choice.lower() == "b":
        Paper()
    elif choice.lower() == "c":
        Sissors()
    else:
        print("That was not a valid option!")
        return

def rockpapersissorsrandom()
    print("Pick one of the following:\n")
    print("(a) Rock, (b) Paper, (c) Sissors")
    choice = input()

    if choice.lower() == "a":
        Rock()
    elif choice.lower() == "b":
        Paper()
    elif choice.lower() == "c":
        Sissors()
    else:
        print("That was not a valid option!")
        return

def Rock():
    print("ROCK!")
    
