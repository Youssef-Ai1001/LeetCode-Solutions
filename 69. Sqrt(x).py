from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:

        sqrt = 0

        for i in range(1, x + 1):
            if i * i > x:
                return sqrt
            sqrt = i
        return sqrt


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (24, 4),
        (25, 5),
        (100, 10),
        (2147395599, 46339),
    ]

    for x, expected in test_cases:
        result = s.mySqrt(x)
        print(f"Input: x = {x}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"✓ Pass" if result == expected else f"✗ Fail")
        print("-" * 30)
