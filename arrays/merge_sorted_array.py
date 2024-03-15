from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    while i < m:
        if nums1[i] == nums2[j]:
            j += 1
        elif nums1[i] <= nums2[j]:
            # shift_elems_to_right(nums1, i+1)
            # nums1[i+1] = nums2[j]
            i += 1
        else:
            shift_elems_to_right(nums1, i)
            nums1[i] = nums2[j]
            i += 1
    print(nums1)


def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    for i, el in enumerate(nums1):
        if el == 0:
            nums1[i] = nums2[j]
            j += 1
    nums1 = sorted(nums1)
    print(nums1)


def shift_elems_to_right(arr: List[int], idx: int) -> None:
    j = len(arr) - 1
    while j > idx+1:
        arr[j] = arr[j-1]
        j -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 4, 5]
m = 3
n = 3
merge(nums1=nums1, nums2=nums2, m=m, n=n)
