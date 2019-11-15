from decimal import Decimal

# Compound Interest calculator
# Returns the initial deposit (principal) and the invested final value
# Initial amount (principal = p)
p = int(input("Please give an initial deposit amount:\n"))

# Annual percentage rate
apr = int(input("Now input your APR (%):\n"))
apr/=100
# Years to invest the principal
y = int(input("How long do you want to invest:\n"))
# Formula for investment:
endval = p*(1+apr)**y
endval = Decimal(endval)

output = round(endval,2)
print("The end value after {} years, with an initial deposit of {}, is\n{}".format(y,p,output))
# Percentage increase
