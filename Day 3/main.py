import re

with open('input.txt', 'r') as file:
    lines = file.read()
    
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, lines)

    
result = 0

for match in matches:
    num1 = int(match[0])  
    num2 = int(match[1])
    result += num1 * num2 

print(result)
    