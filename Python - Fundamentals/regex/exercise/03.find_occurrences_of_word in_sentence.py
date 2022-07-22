import re

text = input()
word = 'there'

print(len(re.findall(word, text)))