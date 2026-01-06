from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        set_nums = set()

        for i in nums:

            if i not in set_nums:
                set_nums.add(i)

            else:
                return True

        return False


if __name__ == "__main__":
    s = Solution()

    tests = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
    ]

    for t in tests:
        nums = t.copy()
        print("Input:", nums)
        print("Result:", s.containsDuplicate(nums))
        print("-" * 30)
