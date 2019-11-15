p = float(input("Input the principle:"))
ar = float(input("now the annual percentage rate:"))
years = float(input("and now the number of years to invest the principle:"))

apr = ar/100 #turning rate into % rate
endvalue = p * ((1+apr)**years) # calculate end value

print("The end value after {} years is {}".format(years,endvalue))

gain = endvalue-p #gain
perchange = (gain/p) * 100 #percentage change
print("The percentage increase after {} years is {}".format(years,perchange))
