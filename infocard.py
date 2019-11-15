#personal info card

name1=str(input("What is your First name?\n Name:"))
name2=str(input("What is your Second name?\n Name:"))
age=int(input("What is your age?\n Age:"))
bday=str(input("When is your birthday? (any format is OK) \n Birthday:"))
height=str(input("What is your height? (in feet and inches)\n Height:"))
favan=str(input("What is your favourite animal? \n Favourite animal:"))

print("\n\n\n****************")
print("{} {}'s Information card:".format(name1, name2))
print("Age: {} years".format(age))
print("Birthday: {}".format(bday))
print("Height: {}".format(height))
print("Fun Fact: {} {}'s favourite animal is a {}!".format(name1,name2, favan))
print("****************")