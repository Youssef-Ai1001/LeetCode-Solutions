from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


if __name__ == "__main__":
    s = Solution()

    tests = [
        [3, 0, 1],
        [0, 1],
    ]

    for t in tests:
        nums = t.copy()
        print("Input:", nums)
        print("Result:", s.missingNumber(nums))
        print("-" * 30)
