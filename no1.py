# Two Sum
# wrong
# wrong
# looked at solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # looked at solution
    dictionary = {}
    for i in range(len(nums)):
        # If our number exists in dictionary then it has been found
        if nums[i] in dictionary:
            # Answer found because Y = Target - X
            # Return the indices of X and Y
            return [dictionary[nums[i]], i]
            # dictionary[Target - X] = index of X
        dictionary[target - nums[i]] = i
