print("\nwelcome to the tip calculator.")
amount = float(input("what is the total bill? $"))
percentage = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
party = int(input("How many people are splitting the bill? "))

tip_percentage = float((percentage) / 100 + 1)
total_tip = round((amount/party)*tip_percentage,2)

print(f"\nIf the bill is split between {party} people, with a {percentage}% tip.")
print(f"Each person should pay ${total_tip}")
