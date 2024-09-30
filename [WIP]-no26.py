from typing import List

def removeDuplicates(nums: List[int]) -> int:
    seen = False
    for i, num in enumerate(nums):
        if seen:
            nums.pop(i)
        else:
            seen = True

print(removeDuplicates([1,2,3]))