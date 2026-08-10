class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _freqElement(s: str):
            chars = [0] * 26
            for elem in s:
                chars[ord(elem) - ord('a')] += 1
            return chars

        result = {}

        for elem in strs:
            freq = tuple(_freqElement(elem))
            if freq not in result:
                result[freq] = []
            result[freq].append(elem)

        return list(result.values())
        
