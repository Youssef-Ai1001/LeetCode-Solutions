from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(S: str):
            ans = []

            for c in S:
                if c != "#":
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(s) == build(t)


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
        ("ab##", "c#d#", True),
        ("y#fo##f", "y#f#o##f", True),
        ("", "", True),
        ("#", "", True),
        ("a", "a", True),
        ("a", "b", False),
    ]

    for s1, s2, expected in test_cases:
        result = s.backspaceCompare(s1, s2)
        print(f"Input: s = \"{s1}\", t = \"{s2}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        assert result == expected, f"Test failed! Expected {expected}, got {result}"
        print("-" * 50)
