from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        return list(set(range(1, len(nums) + 1)) - set(nums))


test = Solution()
print(test.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
