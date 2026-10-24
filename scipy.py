# Working with list

consumptions = [
    12.5, 18.2, 9.6, 24.1, 16.8, 31.2, 14.5, 8.9, 22.4, 19.7
]

# 1. Average
average_daily_consumption = sum(consumptions)/len(consumptions)
print(average_daily_consumption)

# 2. min/max
max_consumption = max(consumptions)
min_consumption = min(consumptions)

print(max_consumption)
print(min_consumption)

# 3 consumption > 18kw
household = list(filter(lambda consumption: consumption > 18.0, consumptions))
print(household)


house_hold = [consumption for consumption in consumptions if consumption > 18.0]
print(house_hold)


high_consumption = []
for num in consumptions:
    if num > 18:
        high_consumption.append(num)

print(high_consumption)

# 4. household > average
average = sum(consumptions)/len(consumptions)

count = 0
for i in consumptions:
    if i > average:
        count +=1

print(count)


# 5. python vs numpy for larger readings
# i will make use of numpy for higher number of readings because of its efficiency in complex calculation
