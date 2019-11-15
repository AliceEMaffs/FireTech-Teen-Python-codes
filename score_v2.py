
def display_results(score):
	if score > 90:
		print("{} points! Fantastic job!!".format(score))
	elif score > 80:
		print("{} points! Great!".format(score))
	elif score > 70:
		print("{} points! Not too bad!".format(score))
	elif score > 60:
		print("{} points! We could do better!".format(score))
	elif score > 50:
		print("{} points! Almost!".format(score))
	else:
		print("{} is not so good. Better luck next time!".format(score))

print("Example 1")
		
userinput = int(input("What did you get?"))
display_results(userinput)

print("*********************")
print("Example 2")
scores = [34, 55, 98, 73, 65, 88, 10]

for mark in scores:
	display_results(mark)
	
print("*********************")
print("Example 3")

def square_and_add_three(value):
	answer = (value * value) + 3
	return answer
	print("Did I make it?")

my_value = square_and_add_three(12)
print(my_value)

print("*********************")
print("Example 4")

print("x \t f(x)")
for x in range(-5, 6):
	fx = square_and_add_three(x)
	print("{} \t {}".format(x, fx))
	
	
print("*********************")
print("Example 5\n")
def main():
	fun1()
	fun2()
	fun3()
	fun1()
	fun3()
	
def fun1():
	print("This is function 1")
	
def fun2():
	print("This is function 2")
	
def fun3():
	print("This is function 3")
	
main()

print("*********************")
print("Example 6\n")

print("Factorial example")
def factorial_func(n):
	num = 1
	while n >= 1:
		num = num * n
		n = n - 1
	print(num)
	return num
	
number = int(input("Enter a number to calculate the factorial:\n"))
factorial_func(number)
	
