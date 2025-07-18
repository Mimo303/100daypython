#test yourself how much you know table 
score=0
for i in range(1,11):
  
  if table_name*i==int(input(f"enter the value of {table_name}*{i}: ")):
    score+=1
  else:
    print()

if score==10:
  print("woooowww, guess you learned your table well 🍫🍫🍫🍫🍫🍫")

print(f"your total score is {score} out of 10 is " )