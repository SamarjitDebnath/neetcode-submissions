class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)

        char_map = [0] * 26

        base = ord('a')
        for i in range(n):
            char_map[ord(s[i]) - base] += 1
            char_map[ord(t[i]) - base] -= 1

        return all(v == 0 for v in char_map)