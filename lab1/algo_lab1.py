def return_indexes_for_target(nums_def, target_def):
    nums_indexes = {}
    result_def = []

    for i, num in enumerate(nums_def):
        complement = target_def - num

        if complement in nums_indexes:
            result_def.append([nums_indexes[complement], i])

        nums_indexes[num] = i

    return result_def


nums = [1, 9, 5, 6, 8, 4]
target = 9
result = return_indexes_for_target(nums, target)

if not result:
    print(-1)
else:
    for indexes in result:
        index1, index2 = indexes
        print({index1}, {index2})
