from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    s = Solution()

    tests = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
    ]

    for t in tests:
        nums = t.copy()
        print("Input:", nums)
        print("Result:", s.singleNumber(nums))
        print("-" * 30)
