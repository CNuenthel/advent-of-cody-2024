import re

"""
AI Prompts Used:

1.  Gib regex

"""

with open("day3_input.txt", "r") as f:
    data = f.read()

# Forking regex
pattern = r"mul\(-?\d+,-?\d+\)"

matches = re.findall(pattern, data)

vals = []
for match in matches:
    nums = match.split(",")
    l_num = int(nums[0][4:])
    r_num = int(nums[1][:-1])
    vals.append(l_num*r_num)

print(sum(vals))









