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


test = Solution()
print(test.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
