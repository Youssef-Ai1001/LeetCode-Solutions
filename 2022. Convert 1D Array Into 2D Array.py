from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        result = []
        start = 0

        if m * n == len(original):
            for _ in range(m):
                row = original[start : start + n]
                result.append(row)
                start += n
        else:
            return []
        return result


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([1, 2, 3, 4], 2, 2),
        ([1, 2, 3], 1, 3),
    ]

    for original, m, n in tests:
        print("Input:", original, "m=", m, "n=", n)
        print("Result:", s.construct2DArray(original=original, m=m, n=n))
        print("-" * 30)
