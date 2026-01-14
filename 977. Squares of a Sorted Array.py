from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        sqr_nums = []
        for i in nums:
            sqr_nums.append(i**2)
        return sorted(sqr_nums)


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Example with negatives and positives
    assert solution.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    print("Test 1 passed: [-4,-1,0,3,10] -> [0,1,9,16,100]")

    # Test Case 2: All negative numbers
    assert solution.sortedSquares([-7, -3, -1]) == [1, 9, 49]
    print("Test 2 passed: [-7,-3,-1] -> [1,9,49]")

    # Test Case 3: All positive numbers
    assert solution.sortedSquares([1, 2, 3]) == [1, 4, 9]
    print("Test 3 passed: [1,2,3] -> [1,4,9]")

    # Test Case 4: Single element
    assert solution.sortedSquares([0]) == [0]
    print("Test 4 passed: [0] -> [0]")

    # Test Case 5: Mixed with duplicates
    assert solution.sortedSquares([-2, -2, 0, 2]) == [0, 4, 4, 4]
    print("Test 5 passed: [-2,-2,0,2] -> [0,4,4,4]")

    print("\nAll test cases passed!")
