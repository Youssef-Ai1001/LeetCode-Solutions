from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # LeetCode typically expects the missing numbers in ascending order.
        return sorted(set(range(1, len(nums) + 1)) - set(nums))


if __name__ == "__main__":
    s = Solution()

    # Test Cases
    assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    print("Test 1 passed: [4,3,2,7,8,2,3,1] -> [5,6]")

    assert s.findDisappearedNumbers([1, 1]) == [2]
    print("Test 2 passed: [1,1] -> [2]")

    # No missing numbers
    assert s.findDisappearedNumbers([1, 2, 3, 4, 5]) == []
    print("Test 3 passed: [1,2,3,4,5] -> []")

    # All duplicates except one number
    assert s.findDisappearedNumbers([2, 2, 2, 2]) == [1, 3, 4]
    print("Test 4 passed: [2,2,2,2] -> [1,3,4]")

    # Minimal size
    assert s.findDisappearedNumbers([1]) == []
    print("Test 5 passed: [1] -> []")

    # (Optional) out-of-constraint case, but should still behave sensibly
    assert s.findDisappearedNumbers([]) == []
    print("Test 6 passed: [] -> []")

    print("\nAll test cases passed!")
