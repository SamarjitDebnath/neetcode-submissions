class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array = {0: 1}
        total = 0
        count = 0
        for num in nums:
            total += num
            count += sub_array.get(total-k, 0)
            sub_array[total] = 1 + sub_array.get(total, 0)

        return count