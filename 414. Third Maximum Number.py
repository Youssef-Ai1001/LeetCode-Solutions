from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

######## Solution 1
        unique_list = sorted(list(set(nums)))

        if len(unique_list) < 3:
            return max(unique_list)
        else:
            return unique_list[-3]


test = Solution()
print(test.thirdMax(nums=[2]))
