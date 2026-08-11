class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = [0] * 26
        groups = {}

        base = ord('a')
        for s in strs:
            for elem in s:
                chars[ord(elem) - base] += 1
            key = tuple(chars)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
            
            chars = [0] * 26

        return list(groups.values())
