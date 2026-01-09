from typing import Any, List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        seen = set()
        
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [10, 2, 5, 3] -> True (5 * 2 = 10)
    assert solution.checkIfExist([10, 2, 5, 3]) == True
    
    # Test case 2: [3, 1, 7, 11] -> False
    assert solution.checkIfExist([3, 1, 7, 11]) == False
    
    # Test case 3: [7, 1, 14, 11] -> True (7 * 2 = 14)
    assert solution.checkIfExist([7, 1, 14, 11]) == True
    
    print("All test cases passed!")
        