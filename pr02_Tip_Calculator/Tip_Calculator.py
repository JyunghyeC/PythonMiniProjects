print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
num_of_people = int(input("How many people to split the bill?\n"))

calculated_tip = (percentage / 100) + 1.0

result = round((bill * calculated_tip) / num_of_people, 2)

print(f"Each person should pay: ${result}")
