# Time module, countdown!!
import time # import the time module
import datetime 

# asctime puts the time entered in a nice format
# gmtime gets the Greenwich mean time
# need to use time.(something) to access these from the 'time' library
now = time.gmtime()
print(now)
#now = time.asctime(now)
now = time.asctime(now) 
print(now)




print("What is your birthday?")
y = input("Year?:")
m = input("Month:")
d = input("Day:")

