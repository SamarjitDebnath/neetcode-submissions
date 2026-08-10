class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hashmap approach
        freq = defaultdict(int)

        for elem in nums:
            freq[elem] += 1

        res = []
        for k, v in freq.items():
            if v > math.floor(len(nums) / 3):
                res.append(k)

        return res
