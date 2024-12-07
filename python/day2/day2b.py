import copy

"""
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""

with open("day2_input.txt", "r") as f:
    data = f.read()

rows = data.splitlines()


def check_row(num_list: list) -> bool:
    greater_than = None
    less_than = None

    # Determine if increasing or decreasing
    for i in range(len(num_list) - 1):

        # Calc diff and check for unsafe
        diff = abs(num_list[i + 1] - num_list[i])
        print(diff)
        if not 0 < diff < 4:
            return False

        # If consecutive number is greater
        if num_list[i + 1] > num_list[i]:

            # But decreasing already flagged...
            if less_than:
                return False

            # Num is < 3 and > 0 and consecutive num is greater, we set increasing status
            greater_than = True

        # Greater than is flagged, but consecutive number isn't greater than, we set unsafe
        elif greater_than:
            return False

        # Not flagged as increasing, then we must be decreasing
        else:
            less_than = True

    # Numbers remained increasing or decreasing and stayed within diff limits
    return True

bads = []
count = 0
for row in rows:
    nums = [int(num) for num in row.split(" ")]
    if check_row(nums):
        # count += 1
        continue
    else:
        bads.append(nums)
        for num in nums:
            new_nums = copy.deepcopy(nums)
            new_nums.remove(num)
            if check_row(new_nums):
                count += 1
                break

print(bads)



