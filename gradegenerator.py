# Grade generator 
test=input("enter the name of the Test ")
total_marks=int(input("Enter the total Marks of the test: "))
your_marks=float(input("Marks obtained: "))
percentage=(your_marks/total_marks)*100
round_percent=round(percentage,2)
if percentage>=90 and percentage<=100:
  print("----------------------------------------------------------------------------")
  print(f"your percentage is {round_percent} and you have got A+ grade 🍟🌭🍿")
  print("-----------------------------------------------------------------------------")
elif percentage>=80 and percentage<=89:
  print("-----------------------------------------------------------------------------")
  print(f"your percentage is {round_percent} and you have got A grade 🍩")
  print("------------------------------------------------------------------------------")
elif percentage>=70 and percentage<=79:
  print("-------------------------------------------------------------------------------")
  print(f"your percnetage is {round_percent} and you have got B garde 🍭")
  print("-------------------------------------------------------------------------------")
elif percentage>=60 and percentage<=69:
  print("-------------------------------------------------------------------------------")
  print(f"your percenatge is {round_percent} and you have got C grade 🍫")
  print("-------------------------------------------------------------------------------")
elif percentage>=50 and percentage<=59:
  print("-------------------------------------------------------------------------------")
  print(f"your percentage is {round_percent} and you have got D grade 🍬")
  print("-------------------------------------------------------------------------------")
elif percentage <50:
  print(f"You have got U grade ::::: ----Bettter luck next time-------🍰🍰🍰")
  print("--------------------------------------------------------------------------------")
else:
  print("Invalid input 😑😑🤨")
