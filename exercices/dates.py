import random
import math
from datetime import datetime
from datetime import timedelta

print (random.randrange (0,200))

print ("Arrondi supérieure : " , math.ceil(3.6))
print ("Arrondi supérieure : " , math.floor(3.6))

print ("Arrondi décimal: " , round(3.67876, 3))

print (datetime(2000, 1, 1))

print (datetime.now())
print (datetime.now().time())
print (datetime.now().year)
print (datetime.now().month)
print (datetime.now().day)
print (datetime.now().hour)
print (datetime.now().minute)
print (datetime.now().second)
print (datetime.now().microsecond)
print (datetime.now() - datetime(2000, 1, 1))
print (datetime.now() + timedelta(days=15))

print ("formatage: " ,datetime.now().strftime("%Y-%m-%d %H:%M"))

print ("Current year: ", datetime.now().strftime("%Y"))
print ("Month of year: ", datetime.now().strftime("%B"))
print ("Week number of the year: ", datetime.now().strftime("%W"))
print ("Weekday of the week: ", datetime.now().strftime("%w"))
print ("Day of year: ", datetime.now().strftime("%j"))
print ("Day of the month : ", datetime.now().strftime("%d"))
print ("Day of week: ", datetime.now().strftime("%A"))

