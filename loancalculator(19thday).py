#principal=1000
#apr=5/100
#time=10
amount=int(input("borrowing amount: "))
apr=float(input("enter the interest rate(give it in decimal): "))
time=int(input("enter the momentary period(only in year): "))
for time in range(1,time+1):
  amount+=amount*apr
  print("-----------------------------------------------")
  print(amount , "is the amount after", time, "year"  "$_$")
  print("-----------------------------------------------")
  print()
  if time==10:
    print(">>>>Your total amount after 10 years is ", amount )