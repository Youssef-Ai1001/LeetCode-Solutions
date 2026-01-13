from typing import Any, List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        count = 0
        expected = sorted(heights)

        for i, j in zip(heights, expected):
            if i != j:
                count += 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Example from LeetCode
    # Input: [1,1,4,2,1,3]
    # Expected: 3 (indices 2, 4, and 5 are in wrong positions)
    assert solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3
    print("Test 1 passed: [1,1,4,2,1,3] -> 3")
    
    # Test Case 2: Already sorted array
    assert solution.heightChecker([1, 2, 3, 4, 5]) == 0
    print("Test 2 passed: [1,2,3,4,5] -> 0")
    
    # Test Case 3: Reverse sorted array
    assert solution.heightChecker([5, 4, 3, 2, 1]) == 4
    print("Test 3 passed: [5,4,3,2,1] -> 4")
    
    # Test Case 4: Single element
    assert solution.heightChecker([1]) == 0
    print("Test 4 passed: [1] -> 0")
    
    # Test Case 5: All elements the same
    assert solution.heightChecker([2, 2, 2, 2]) == 0
    print("Test 5 passed: [2,2,2,2] -> 0")
    
    # Test Case 6: Two elements swapped
    assert solution.heightChecker([2, 1]) == 2
    print("Test 6 passed: [2,1] -> 2")
    
    # Test Case 7: Multiple duplicates
    assert solution.heightChecker([1, 2, 1, 2, 1, 1, 1, 2, 1]) == 4
    print("Test 7 passed: [1,2,1,2,1,1,1,2,1] -> 4")
    
    print("\nAll test cases passed!")
    