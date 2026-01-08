from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(f"Test 1: k = {k1}, nums = {nums1[:k1]}")
    
    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(f"Test 2: k = {k2}, nums = {nums2[:k2]}")
