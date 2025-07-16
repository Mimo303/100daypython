# cheat custom table , 
#print any table 

whichtable=int(input("which table: ")) # enter the table you want to print 
start_at=int(input("enter where to start: ")) # generally enter 1 but if you want to start directly from 5 or any number you can do that too
end_at=int(input("enter where to end: ")) # till where you want to print the table 
increment=int(input("how much to increase by: ")) # generally 1 but if you want to try increasing 2 or 3 .. you can 
print()
print("here is your table: ")
print()
for i in range(start_at, end_at+1 ,increment):
  print("|",i*whichtable,"is",i,"times",whichtable ,"|")
