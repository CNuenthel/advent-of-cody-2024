import re

"""
AI Prompts Used:

1.  give me regex to match the string "mul(num,num)"
    where num can be any integer up to any length

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









