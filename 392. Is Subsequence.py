class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Two-pointer approach
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("", "ahbgdc", True),  # empty s is subsequence of any t
        ("abc", "", False),
        ("a", "a", True),
        ("aaaa", "aa", False),
        ("abc", "abc", True),
        ("abc", "aabbcc", True),
    ]

    for s, t, expected in test_cases:
        result = sol.isSubsequence(s, t)
        print(f's = "{s}", t = "{t}"')
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        assert (
            result == expected
        ), f"Test failed for s={s}, t={t}: expected {expected}, got {result}"
        print("-" * 50)
