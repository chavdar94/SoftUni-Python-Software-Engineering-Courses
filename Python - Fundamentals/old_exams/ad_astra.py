import re

text = input()

pattern = r'(#|\|)\w+\1\d+\/\d+\/\d+\1\d+\1'
matches = re.finditer(pattern, text)

foods = [match.group() for match in matches]
print(foods)


