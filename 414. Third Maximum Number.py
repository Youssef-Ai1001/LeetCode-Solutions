from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

######## Solution 1
        # unique_list = sorted(list(set(nums)))

        # if len(unique_list) < 3:
        #     return max(unique_list)
        # else:
        #     return unique_list[-3]

######## Solution 2
        first = second = third = float("-inf")

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

        return third if third != float("-inf") else first


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Example with distinct numbers
    assert solution.thirdMax([3, 2, 1]) == 1
    print("Test 1 passed: [3, 2, 1] -> 1")

    # Test Case 2: Less than three distinct numbers
    assert solution.thirdMax([1, 2]) == 2
    print("Test 2 passed: [1, 2] -> 2")

    # Test Case 3: Duplicates, third distinct exists
    assert solution.thirdMax([2, 2, 3, 1]) == 1
    print("Test 3 passed: [2, 2, 3, 1] -> 1")

    # Test Case 4: All same numbers
    assert solution.thirdMax([2, 2, 2]) == 2
    print("Test 4 passed: [2, 2, 2] -> 2")

    # Test Case 5: Negative numbers with mix
    assert solution.thirdMax([1, -2147483648, 2]) == -2147483648
    print("Test 5 passed: [1, -2147483648, 2] -> -2147483648")

    # Test Case 6: Longer list with duplicates
    assert solution.thirdMax([5, 2, 2, 4, 3, 1]) == 3
    print("Test 6 passed: [5, 2, 2, 4, 3, 1] -> 3")

    # Test Case 7: Already sorted descending
    assert solution.thirdMax([5, 4, 3, 2, 1]) == 3
    print("Test 7 passed: [5, 4, 3, 2, 1] -> 3")

    print("\nAll test cases passed!")
