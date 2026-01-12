from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
######## Solution 1
        # even = []
        # odd = []
        
        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     elif num % 2 == 1:
        #         odd.append(num)
        # return even + odd 
        
        
######## Solution 2
        left = 0 
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Single zero
    nums1 = [0]
    result1 = solution.sortArrayByParity(nums1.copy())
    assert result1 == [0], f"Test Case 1 Failed: Expected [0], got {result1}"
    print("Test Case 1 Passed")

    # Test Case 2: Mixed even and odd
    nums2 = [3, 1, 2, 4]
    result2 = solution.sortArrayByParity(nums2.copy())
    # Only requirement: all evens come before all odds (order within groups can vary)
    assert set(result2[:2]) == {2, 4} and set(result2[2:]) == {3, 1}, \
        f"Test Case 2 Failed: Got {result2}"
    print("Test Case 2 Passed")

    # Test Case 3: All even
    nums3 = [2, 4, 6, 8]
    result3 = solution.sortArrayByParity(nums3.copy())
    assert result3 == [2, 4, 6, 8], f"Test Case 3 Failed: Expected [2, 4, 6, 8], got {result3}"
    print("Test Case 3 Passed")

    # Test Case 4: All odd
    nums4 = [1, 3, 5, 7]
    result4 = solution.sortArrayByParity(nums4.copy())
    assert result4 == [1, 3, 5, 7], f"Test Case 4 Failed: Expected [1, 3, 5, 7], got {result4}"
    print("Test Case 4 Passed")

    # Test Case 5: Includes zero and negatives
    nums5 = [0, -2, -3, 5, 4]
    result5 = solution.sortArrayByParity(nums5.copy())
    # Evens: 0, -2, 4; Odds: -3, 5 (order within groups can vary)
    evens5 = [x for x in result5 if x % 2 == 0]
    odds5 = [x for x in result5 if x % 2 != 0]
    assert set(evens5) == {0, -2, 4} and set(odds5) == {-3, 5} and result5.index(evens5[-1]) < result5.index(odds5[0]), \
        f"Test Case 5 Failed: Got {result5}"
    print("Test Case 5 Passed")

    print("\nAll test cases passed!")