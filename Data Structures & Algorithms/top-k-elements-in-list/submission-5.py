class Solution:
    @staticmethod
    def _get_freq(arr: List[int]) -> Dict[int, int]:
        freq = {}
        for elem in arr:
            freq[elem] = freq.get(elem, 0) + 1
            # if elem in freq:
            #     freq[elem] += 1
            # else:
            #     freq[elem] = 1
        return freq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freqElement = Solution._get_freq(nums)
        sortedFreq = sorted(freqElement, key = lambda x: (-freqElement[x], nums.index(x)))

        return [elem for elem in sortedFreq[:k]]

    