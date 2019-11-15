# Defining and using functions

# Basic syntax
def a_function():
    print("This is my first function!!")
    print("And it keeps going till there is nothing else to do")

a_function()

print("*****")

for i in range(5):
    a_function()

print("\n******")
print("Example 1:\n")

def display_results(score):
    if score > 90:
        print("{} points! Congrats!!".format(score))
    elif score > 80:
        print("{} points! Great job!!".format(score))
    elif score > 70:
        print("{} points! Not too bad!!".format(score))
    elif score > 60:
        print("{} points! Good, but lets get more next time!!".format(score))
    elif score > 50:
        print("{} points! Mm, Not so good!!".format(score))
    else:
      print("{} Is not good at all :(((( dont worry!".format(score))

def print_func(a):
    print(a)

number1 = 5
print_func(number1)
string1= "HEY!"
print_func(string1)

def add_func(a,b):
    c = a + b
    print(c)
    return c

number1 = 4
number2 = 1
add_func(number1, number2)


print("\n*****")
print("Example 2:\n")

scores = [32, 1, 99, 18, 76, 74, 30, 45, 55]

for mark in scores:
    display_results(mark)

print("\n*****")
print("Example 3:\n")

def sq_add_3(x):
    b = x*x + 3
    return b

num1 = sq_add_3(1)
print(num1)


print("***********")
print("Example 4:\n")

def main():
    while True:
        print("Please choose from the following games:")
        print("A: Chess")
        print("B: Tic tac toe")
        print("C: Nuclear War")
        print("X to exit")
        user_choice = input("Pick an option: ")
        if user_choice.upper() == "A":
            chess()
        elif user_choice.upper() == "B":
            tic_tac()
        elif user_choice.upper() == "C":
            war()
        elif user_choice.upper() == "X":
            print("Sad to see u go :( ")
            break
        else:
            print("Opps, no option available, please enter again")

def chess():
    print("CHESS YAY!")
def tic_tac():
    print("The only option is not to play!")
def war():
    print("SOS!! BOOOOOOM")

main()


