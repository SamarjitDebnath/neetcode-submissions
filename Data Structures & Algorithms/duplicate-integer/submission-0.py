class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for elem in nums:
            if elem in freq:
                freq[elem] += 1
                return True
            else:
                freq[elem] = 1
        return False