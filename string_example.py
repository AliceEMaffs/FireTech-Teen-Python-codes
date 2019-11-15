allys_string = "HI, im ally!"
c = len(allys_string)
print("Allys string is {} characters long".format(c))

print("This is ", len(allys_string), "long")

age = input("Please enter how many years old you are: ")
print("age is currently: ", type(age))

#it is common to cast a variable to another data type in Python
#then store it back into the same name
age = int(age)
print("age is now: ", type(age))

#Add 10 years to the age and store it back into the same variable name
age = age + 10
print("In ten years time you will be: {} years old".format(age))

#Sometimes we have to cast an interger to a string to output it
print("The age explicitly cast to an integer: " + str(age))