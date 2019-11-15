import datetime

xmas = datetime.date(2019,12,25)

daystillxmas = xmas - datetime.date.today()

print("There are {} till xmas".format(daystillxmas))

print("***************************")
print("Now lets choose any date")

year = int(input("Input a year: "))
month = int(input("Input a month: "))
day = int(input("Input a day: "))

newdate = datetime.date(year,month,day)

print("You inputted {}/{}/{}".format(day,month,year))

countdown = newdate - datetime.date.today() 
print("It is {} till your selected date!".format(countdown))

