# Challenge 1, Session 1, Day 2

input_string = input("Please enter any thing!")
length_string = len(input_string)
mirror = input_string[::-1]

if length_string <= 10:
    print("The input string is less than or equal to 10!")      

else:
    print("It is more than 10!")

if input_string.isupper():
    print("The string is UPPER")
else:
    print("The string contains a lower case!")


if mirror == input_string:
    print("its a palindrome!")

else:
    print("Its not a palindrome!!")
