tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill = float(input("What was the total bill? "))
tip_per_head = bill*(1+tip/100)/people
print(f"Each person should pay: {round(tip_per_head, 2)}")