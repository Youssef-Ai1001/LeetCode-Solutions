from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # Input:  arr = [1,0,2,3,0,4,5,0]
        # Output:       [1,0,0,2,3,0,0,4]
        #
        # Idea:
        # - Count how many zeros will be duplicated.
        # - Use two pointers from the end: one on the original array,
        #   and one on the "virtual" expanded array of length n + zeros.
        # - Copy elements backwards, writing only when the write-index
        #   is within the bounds of the original array.

        n = len(arr)
        zeros = arr.count(0)

        i = n - 1                 # read index
        j = n + zeros - 1         # write index in virtual expanded array

        while i >= 0 and j >= 0:
            # Copy current element if target index is inside bounds
            if j < n:
                arr[j] = arr[i]

            # If the element is zero, we need to "duplicate" it:
            # write another zero just before j.
            if arr[i] == 0:
                j -= 1
                if j < n and j >= 0:
                    arr[j] = 0

            i -= 1
            j -= 1


if __name__ == "__main__":
    # Basic tests for 1089. Duplicate Zeros
    solution = Solution()

    test_cases = [
        # (input, expected)
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),                      # no zeros
        ([0, 0, 0], [0, 0, 0]),                      # all zeros, truncated
        ([1, 0, 0, 2], [1, 0, 0, 0]),                # multiple zeros in a row
        ([0, 1], [0, 0]),                            # zero at the beginning
        ([1, 0], [1, 0]),                            # zero at the end
    ]

    for idx, (arr, expected) in enumerate(test_cases, 1):
        original = list(arr)
        solution.duplicateZeros(arr)
        assert arr == expected, f"Test {idx} failed: input={original}, got={arr}, expected={expected}"

    print("All tests for '1089. Duplicate Zeros' passed.")