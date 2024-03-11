from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while i < m:
        if nums1[i] > nums2[i]:
            shift_elems_to_right(nums1, i)
            nums1[i] = nums2[i]
        elif nums1[i] < nums2[i]:
            pass
        else:
            shift_elems_to_right(nums1, i)
            nums1[i] = nums2[i]
        i += 1
    print(nums1)


def shift_elems_to_right(arr: List[int], idx: int) -> None:
    # shift everything to the right
    j = len(arr) - 1
    while j > idx+1:
        arr[j] = arr[j-1]
        j -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 4, 5]
m = 3
n = 3
merge(nums1=nums1, nums2=nums2, m=m, n=n)
