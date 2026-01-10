from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        i = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == len(arr) - 1:
            return False

        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        return i == len(arr) - 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [2, 1] -> False (too short)
    assert solution.validMountainArray([2, 1]) == False
    
    # Test case 2: [3, 5, 5] -> False (equal elements)
    assert solution.validMountainArray([3, 5, 5]) == False
    
    # Test case 3: [0, 3, 2, 1] -> True (valid mountain)
    assert solution.validMountainArray([0, 3, 2, 1]) == True
    
    # Test case 4: [0, 1, 2, 3] -> False (only increasing)
    assert solution.validMountainArray([0, 1, 2, 3]) == False
    
    # Test case 5: [3, 2, 1, 0] -> False (only decreasing)
    assert solution.validMountainArray([3, 2, 1, 0]) == False
    
    print("All test cases passed!")

