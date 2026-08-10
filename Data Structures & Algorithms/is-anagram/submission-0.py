class Solution:
    @staticmethod
    def _get_frequency(s: str):
        freq = {}
        for elem in s:
            if elem in freq:
                freq[elem] += 1
            else:
                freq[elem] = 1
        
        return freq

    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = Solution()._get_frequency(s)
        tFreq = Solution()._get_frequency(t)

        return sFreq == tFreq