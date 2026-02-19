from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = []
        max_candies = max(candies)

        for i in candies:
            if (i + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result


if __name__ == "__main__":
    s = Solution()

    # Simple test cases
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))
    print(s.kidsWithCandies([12, 1, 12], 10))
