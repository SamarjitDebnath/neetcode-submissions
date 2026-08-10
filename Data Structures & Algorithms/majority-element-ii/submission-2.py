class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hashmap approach
        # freq = defaultdict(int)

        # for elem in nums:
        #     freq[elem] += 1

        # res = []
        # for k, v in freq.items():
        #     if v > math.floor(len(nums) / 3):
        #         res.append(k)

        # return res
        
        # voting algo
        freq = defaultdict(int) # at max 2 elements
        
        for elem in nums:
            # max n elements
            freq[elem] += 1

            if len(freq) <= 2:
                continue

            freq_update = defaultdict(int)
            for n, f in freq.items():
                # max 2 elems
                if f > 1:
                    freq_update[n] = (f - 1)
            freq = freq_update

        res = []
        # max 2 times
        for num in freq:
            if nums.count(num) > len(nums) // 3:
                # liner time -> O(2 * n) ~ O(n)
                res.append(num)
        return res
