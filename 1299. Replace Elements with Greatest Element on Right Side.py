from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):

            current = arr[i]
            arr[i] = max_so_far

            max_so_far = max(max_so_far, current)

        return arr


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Example from problem description
    arr1 = [17, 18, 5, 4, 6, 1]
    expected1 = [18, 6, 6, 6, 1, -1]
    result1 = solution.replaceElements(arr1.copy())
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed")
    
    # Test Case 2: Single element array
    arr2 = [400]
    expected2 = [-1]
    result2 = solution.replaceElements(arr2.copy())
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed")
    
    # Test Case 3: Two elements
    arr3 = [1, 2]
    expected3 = [2, -1]
    result3 = solution.replaceElements(arr3.copy())
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed")
    
    # Test Case 4: All same elements
    arr4 = [3, 3, 3, 3]
    expected4 = [3, 3, 3, -1]
    result4 = solution.replaceElements(arr4.copy())
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Test Case 4 Passed")
    
    # Test Case 5: Decreasing order
    arr5 = [5, 4, 3, 2, 1]
    expected5 = [4, 3, 2, 1, -1]
    result5 = solution.replaceElements(arr5.copy())
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Test Case 5 Passed")
    
    print("\nAll test cases passed!")
