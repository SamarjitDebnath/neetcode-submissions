class Solution:
    @staticmethod
    def _get_frequency(string: str) -> List[int]:
        freq = [0] * 26
        for elem in string:
            freq[ord(elem) - ord('a')] += 1 
        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resGroups = {}
        
        for elem in strs:
            freqElem = tuple(Solution._get_frequency(elem))
            if freqElem not in resGroups:
                resGroups[freqElem] = []
            resGroups[freqElem].append(elem)
        
        return resGroups.values()
        

        