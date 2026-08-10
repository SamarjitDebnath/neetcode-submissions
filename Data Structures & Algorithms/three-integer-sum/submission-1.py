class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # break if element > 0, avoids redundant operations
            if a > 0:
                break
            
            # check for duplicate
            if i > 0 and a == nums[i-1]:
                continue

            # as we've gotten 'a' now we will find 'b' and 'c'
            # using two sum method (two pointers)
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # r -= 1
                    while(l<r) and (nums[l] == nums[l-1]):
                        l += 1

        return res
            