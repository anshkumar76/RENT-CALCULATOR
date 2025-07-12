# Inputs we need from the user.
# Total Rent.
# Total Food ordered for Snacking.
# Electricity unit Spend.
# Charge per unit.
# Persons living in PG.

# Output.
# Total amount you've to pay is

rent = int(input("Enter your PG rent = "))
food = int(input("Enter the amount of food ordered = "))
electricty_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in PG = "))

total_bill = charge_per_unit * electricty_spend

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)