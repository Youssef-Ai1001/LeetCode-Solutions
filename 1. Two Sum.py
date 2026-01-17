from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 3, 7, 2], 9, [3, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    for nums, target, expected in test_cases:
        result = s.twoSum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        assert result == expected, f"Test failed! Expected {expected}, got {result}"
        print("-" * 50)
