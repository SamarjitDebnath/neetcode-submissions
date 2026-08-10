class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def _getFreq(string: str):
            freq = defaultdict(int)

            for elem in string:
                freq[elem] = freq.get(elem, 0) + 1

            return freq

        sFreq = _getFreq(string = s)
        tFreq = _getFreq(string = t)

        return sFreq == tFreq