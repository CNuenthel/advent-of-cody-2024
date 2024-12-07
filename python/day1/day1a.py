import sys

sys.setrecursionlimit(1025)

with open("day1_input.txt", "r") as f:
    data = f.read()

rows = data.splitlines()

left = []
right = []
calcs = []

for item in rows:
    nums = item.split("   ")
    left.append(int(nums[0]))
    right.append(int(nums[1]))


def recursive_subtract(left_list, right_list):
    if not left_list and not right_list:
        return

    num1 = min(left_list)
    num2 = min(right_list)
    calcs.append(abs(num1 - num2))

    left_list.remove(num1)
    right_list.remove(num2)

    recursive_subtract(left_list, right_list)


recursive_subtract(left, right)

print(sum(calcs))
