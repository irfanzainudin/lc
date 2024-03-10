from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            # shift everything to the right
            j = len(arr) - 1
            while j > i+1:
                arr[j] = arr[j-1]
                j -= 1
            # set duplicate
            if i+1 < len(arr):
                arr[i+1] = 0
            i += 1
        i += 1
    print(arr)


arr = [1, 2, 3]
duplicateZeros(arr)
