numbers = input().split()

inverted_numbers = []
for number in numbers:
    number = int(number)
    if number > 0:
        inverted_numbers.append(-abs(number))
    else:
        inverted_numbers.append(abs(number))
print(inverted_numbers)

