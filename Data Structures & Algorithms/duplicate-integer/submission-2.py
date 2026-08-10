class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for elem in nums:
            freq[elem] = freq.get(elem, 0) + 1

        return any(value > 1 for value in freq.values())