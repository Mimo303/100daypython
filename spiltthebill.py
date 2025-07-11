# Spilt the bill calculator
print("💸 Welcome to the Split the Bill Calculator! 💸")
bill = float(input("🧾 Enter your total bill amount: "))
tip = int(input("💡 What % tip would you like to give? (15/18/20): "))
people = int(input("👥 How many people are splitting the bill?: "))

tipp = tip / 100 * bill
total_bill = bill / people
total_amount = total_bill + tipp

print("\n----- Bill Summary -----")
print(f"Total bill: ₹{bill:.2f}")
print(f"Tip percentage: {tip}%")
print(f"Number of people: {people}")
print("------------------------")
print(f"Each person should pay: ₹{total_amount:.2f} 🤑")
print("✨ Thank you for using Split the Bill! ✨")
