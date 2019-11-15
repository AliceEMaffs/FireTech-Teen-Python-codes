
# without a prompt
print("what is your name?\n")
name1 = input()
print("Hello {}, welcome to session 2!".format(name1))


age = input("Please enter how many years old you are: ")
print("Age is currently: ", type(age))

# Casting to change 'str' to 'int'
age = int(age)
print("Age is now: ", type(age))

# Add ten years to the age and store it back into str
age = age + 10
print("In ten years you will be: {} years old".format(age))

# Can sometimes cast an integer back into a string
print("The age is cast back into string: " + str(age))
print("The age type is now: ", type(age))
age = str(age)
print("The age type is now: \n", type(age))
print(age)
age = 1
print(age)
