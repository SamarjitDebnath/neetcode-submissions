class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        base_map = {}

        for i, num in enumerate(nums):
            if (target - num) in base_map:
                return [base_map[target - num], i]
            else:
                base_map[num] = i
        return []