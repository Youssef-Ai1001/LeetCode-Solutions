from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = None
        count = 0
        
        for i in nums:
            if count == 0:
                candidate = i
            
            if i == candidate:
                count += 1
            else:
                count-=1
                
        return candidate 


if __name__ == "__main__":
    test = Solution()

    # Simple test cases
    nums1 = [3]  # single element
    nums2 = [2, 2, 1]  # clear majority 2
    nums3 = [1, 1, 1, 2, 3]  # majority 1
    nums4 = [2, 2, 1, 1, 1, 2, 2]  # your original example, majority 2

    print("nums1:", nums1, "-> majority:", test.majorityElement(nums1))
    print("nums2:", nums2, "-> majority:", test.majorityElement(nums2))
    print("nums3:", nums3, "-> majority:", test.majorityElement(nums3))
    print("nums4:", nums4, "-> majority:", test.majorityElement(nums4))