from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
######## Solution 1 (Two Pointer)
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]  # Swap
            l += 1
            r -= 1



# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic case
    test1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(test1)
    assert test1 == ["o", "l", "l", "e", "h"], f"Test 1 failed: {test1}"
    print("Test 1 passed: ['h', 'e', 'l', 'l', 'o'] -> ['o', 'l', 'l', 'e', 'h']")
    
    # Test Case 2: Two characters
    test2 = ["H", "a"]
    solution.reverseString(test2)
    assert test2 == ["a", "H"], f"Test 2 failed: {test2}"
    print("Test 2 passed: ['H', 'a'] -> ['a', 'H']")
    
    # Test Case 3: Single character
    test3 = ["x"]
    solution.reverseString(test3)
    assert test3 == ["x"], f"Test 3 failed: {test3}"
    print("Test 3 passed: ['x'] -> ['x']")
    
    # Test Case 4: Empty list
    test4 = []
    solution.reverseString(test4)
    assert test4 == [], f"Test 4 failed: {test4}"
    print("Test 4 passed: [] -> []")
    
    # Test Case 5: Even length
    test5 = ["a", "b", "c", "d"]
    solution.reverseString(test5)
    assert test5 == ["d", "c", "b", "a"], f"Test 5 failed: {test5}"
    print("Test 5 passed: ['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']")
    
    # Test Case 6: Odd length
    test6 = ["1", "2", "3", "4", "5"]
    solution.reverseString(test6)
    assert test6 == ["5", "4", "3", "2", "1"], f"Test 6 failed: {test6}"
    print("Test 6 passed: ['1', '2', '3', '4', '5'] -> ['5', '4', '3', '2', '1']")
    
    # Test Case 7: Palindrome (should remain same)
    test7 = ["a", "b", "a"]
    solution.reverseString(test7)
    assert test7 == ["a", "b", "a"], f"Test 7 failed: {test7}"
    print("Test 7 passed: ['a', 'b', 'a'] -> ['a', 'b', 'a']")
    
    # Test Case 8: Mixed case
    test8 = ["A", "B", "c", "D"]
    solution.reverseString(test8)
    assert test8 == ["D", "c", "B", "A"], f"Test 8 failed: {test8}"
    print("Test 8 passed: ['A', 'B', 'c', 'D'] -> ['D', 'c', 'B', 'A']")
    
    print("\nAll test cases passed! ✓")