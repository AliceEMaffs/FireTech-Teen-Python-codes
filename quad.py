import cmath

a = float(input("input the first number: "))
b = float(input("input the second number: "))
c = float(input("input the third number: "))

#quad = a*x + b*(x**2) + c

d = (b**2) - (4*a*c)

sol1 = (-b - cmath.sqrt(d))/(2*a)
sol2 = (-b + cmath.sqrt(d))/(2*a)

print("The solution are {} and {} ".format(sol1, sol2))