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

if __name__ == "__main__":
    s = Solution()

    tests = [
        [0,1,0,3,12],
        [0,0,1],
        [1,2,3],
        []
    ]

    for t in tests:
        nums = t.copy()
        print("Input:", nums)
        s.moveZeroes(nums)
        print("Result:", nums)
        print('-' * 30)