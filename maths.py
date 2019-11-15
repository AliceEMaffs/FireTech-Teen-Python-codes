#Input our numbers
first_value=int(input("Please enter a whole number:"))
second_value=int(input("Now a second: "))

#Remind the user what they put
print("You entered {} and {}.".format(first_value,second_value))

#Now do some maths!!
print("Adding: {} + {} = {}".format(first_value,second_value,first_value+second_value))
print("Subtracting: {} - {} = {}".format(first_value,second_value,first_value-second_value))
print("Multiplying: {} x {} = {}".format(first_value,second_value,first_value*second_value))
print("Diving: {} % {} = {}".format(first_value,second_value,first_value/second_value))


print("**********")
print("using %")
print(10%4)
print(10%3)
print("using //")
print(10//4)
print(10//3)

print("using +=")
a = 10
b = 9
print("a =" + str(a))
print("b = " + str(b))
a+=b

print("New value of a =" + str(a))

