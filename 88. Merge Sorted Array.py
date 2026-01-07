from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        result = nums1[0:m] + nums2
        result.sort()
        
        for i in range(len(nums1)):
            nums1[i] = result[i]
            
        # return nums1

if __name__ == "__main__":
    
    nums1=[1,2,3,0,0,0]
    m = 3
    nums2=[2,5,6]
    n=3
    
    test = Solution()
    test.merge(nums1,m,nums2,n)