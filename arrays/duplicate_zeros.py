class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in arr:
            if i == 0:
                print(i)
            else:
                print("not zero")
