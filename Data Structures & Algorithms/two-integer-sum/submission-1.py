class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], index]
            numMap[num] = index

        return []