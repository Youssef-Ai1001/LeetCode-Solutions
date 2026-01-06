from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        return list(set(range(1, len(nums) + 1)) - set(nums))


if __name__ == "__main__":
    s = Solution()

    tests = [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1],
        []
    ]

    for t in tests:
        nums = t.copy()
        print("Input:", nums)
        print("Result:", s.findDisappearedNumbers(nums=nums))
        print('-' * 30)
