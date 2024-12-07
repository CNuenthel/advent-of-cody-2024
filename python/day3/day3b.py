import re

"""
AI Prompts Used:

1. Gib updated regex

"""


def multiply_string(mul_str: str) -> int:
    nums = mul_str.split(",")
    l_num = int(nums[0][4:])
    r_num = int(nums[1][:-1])
    return l_num*r_num


with open("day3_input.txt", "r") as f:
    data = f.read()

pattern = r"mul\(-?\d+,-?\d+\)|do\(\)|don't\(\)"

matches = re.findall(pattern, data)

vals = []
do_indicator = True
for found_str in matches:
    if found_str == "do()":
        do_indicator = True
    elif found_str == "don't()":
        do_indicator = False
    else:
        if do_indicator:
            res = multiply_string(found_str)
            vals.append(res)

print(sum(vals))









