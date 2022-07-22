import re

pattern = r"([A-Za-z]+)<<(\d+\.?\d*)\!(\d)"

command = input()
furniture_count = {}

while command != "Purchase":
    matches = re.findall(pattern, command)
    if matches:
        for match in matches:
            name = match[0]
            price = float(match[1])
            quantity = int(match[2])
            total_price = price * quantity
            furniture_count[name] = total_price

    command = input()
print("Bought furniture:")
if furniture_count:
    for furn in furniture_count:
        print(furn)

total_cost = sum(furniture_count.values())
print(f"Total money spend: {total_cost:.2f}")