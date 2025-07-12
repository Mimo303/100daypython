# How many second in a year 
days=(input("is this a leap year?(y/n): "))
#1min=60 sec
#1hr=60min
#1 day=24 hr
#31 days=1 month
#12 months = 1 year 
# 1 year =365 days 
#leap year=366 days 
if days.lower()=="n":
  print("If its not a leap then it will have:")
  print(60*60*24*365,"seconds in a year ")
elif days.lower()=="y":
  print("If its a leap year then it will have:")
  print(60*60*24*366,"seconds in a year")
else:
  print("please enter a valid input")