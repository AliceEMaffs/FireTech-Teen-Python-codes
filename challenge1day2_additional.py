# challenge 1 session 2 day 2
# The length of an inputted string is less than or equal to 10

input_string = input("Please input a string: ")

#1
length_less_or_eq = len(input_string) <= 10

if length_less_or_eq == True:
	print("The length of string is less than 10 characters.")
else:
	print("The length of string is more than 10 characters.")
#2	
if input_string == "burmese python" or input_string == "python":
	print("The inputted string is equal to burmese python or python")
else:
	print("It is not equal to burmese python or python")

#3
if input_string.isupper():
	print("The input string is upper case!")
else:
	print("The input string is lower case")
#4 is inputted string a palindrome
if input_string[::-1] == input_string:
	print("The string is a palindrome!")
else:
	print("It is not a palindrome :( ")
	
#5 input number is integer
input_num = int(input("Please input any number: "))
if type(input_num) != int:
	print("It is not of type integer!")
else:
	print("It is of type integer")
	