from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                current += 1
                max_ones = max(max_ones, current)
            else:
                current = 0

        return max_ones


if __name__ == "__main__":
    s = Solution()

    tests = [
        # format: (input, expected)
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([1], 1),
        ([0], 0),
        ([1, 0, 1, 0, 1, 0, 1], 1),
        ([], 0),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = s.findMaxConsecutiveOnes(nums)
        print(f"Test {i}: input={nums}, expected={expected}, got={result}, pass={result == expected}")