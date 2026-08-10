class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def _getFrequency(num_list: list) -> dict:
            freq = {}
            for elem in num_list:
                freq[elem] = freq.get(elem, 0) + 1
            return freq
        
        if not nums: return []

        frequency = _getFrequency(nums)
        sortedFreq = sorted(frequency, key = lambda x: (-frequency[x], nums.index(x)))

        return sortedFreq[:k]