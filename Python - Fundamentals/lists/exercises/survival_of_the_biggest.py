numbers = input().split()
numbers_to_remove = int(input())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for remove in range(numbers_to_remove):
    numbers.remove(min(numbers))

for strings in range(len(numbers)):
    numbers[strings] = str(numbers[strings])

print(", ".join(numbers))