from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = []
        non_zero = []

        for x in nums:
            if x == 0:
                zeros.append(0)
            else:
                non_zero.append(x)

        nums[:] = non_zero + zeros
