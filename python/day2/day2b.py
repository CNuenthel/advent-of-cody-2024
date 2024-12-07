def check_row(num_list):
    increasing = None
    for i in range(len(num_list) - 1):
        diff = abs(num_list[i + 1] - num_list[i])
        if not 0 < diff < 4:
            return False
        
        if num_list[i + 1] > num_list[i]:
            if increasing is False:
                return False
            increasing = True
        elif num_list[i + 1] < num_list[i]:  # Descending trend
            if increasing is True:
                return False
            increasing = False
    return True


def is_safe_with_dampener(num_list):
    if check_row(num_list):
        return True
    for i in range(len(num_list)):
        temp_list = num_list[:i] + num_list[i + 1:]
        if check_row(temp_list):
            return True
    return False


# Main processing
with open("day2_input.txt", "r") as f:
    rows = f.read().splitlines()

count = 0
for row in rows:
    nums = [int(num) for num in row.split()]
    if is_safe_with_dampener(nums):
        count += 1

print(count)
