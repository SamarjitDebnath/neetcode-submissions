class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        maxf = 0

        l = 0
        res = 0

        for r in range(len(s)):
            char[s[r]] = char.get(s[r], 0) + 1
            maxf = max(maxf, char[s[r]])

            while ((r - l + 1) - maxf) > k:
                char[s[l]] -= 1
                l += 1
            res = max((r-l+1), res)

        return res