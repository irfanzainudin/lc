# Find First and Last Position of Element in Sorted Array
# wrong
# wrong
# accepted

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if target not in nums:
        return [-1, -1]
    if len(nums) == 1:
        return [0, 0]
    result = []
    for idx, x in enumerate(nums):
        if x == target:
            result.append(idx)
    return [result[0], result[len(result) - 1]]


print(searchRange(nums=[1, 2, 2, 3], target=2))
print(searchRange(nums=[2], target=2))
print(searchRange(nums=[2, 2], target=2))
print(searchRange(nums=[2], target=1))
