
def check_if_mono(nums_def):
    down = True
    up = True
    if not nums_def:
        print("List is empty")
        return
    for i in range(len(nums_def) - 1):
        if nums_def[i] > nums_def[i + 1]:
            up = False
        if nums_def[i] < nums_def[i + 1]:
            down = False
    return down or up


nums = [2, 3, 4, 5]
result = check_if_mono(nums)
print(result)
