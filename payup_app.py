print("Welcome to payUp!")


event= input("What was the event or occasion? ")
cost = float(input("how much was it? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g 20 for 20%):").strip("%"))
group_size = int(input("How many people were in you group? "))





service_charge_total= (service_charge/100)*cost

grand_total= service_charge_total+ cost

total_per_person= grand_total / group_size





print()
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charge_total}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total}")
print()
print(f"each person must payUp: ${total_per_person:.2f}")

# Testing the display of username