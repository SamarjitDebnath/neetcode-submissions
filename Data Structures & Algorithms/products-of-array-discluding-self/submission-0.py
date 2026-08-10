class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        res = [0] * len(nums)
        
        # find product and zeros
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1

        # more than 1 zero means product is 0
        if zero_count > 1:
            return res
        
        for index, num in enumerate(nums):
            if zero_count:
                res[index] = 0 if num else product
            else:
                res[index] = product // num

        return res
