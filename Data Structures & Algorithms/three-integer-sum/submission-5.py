class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for idx, elem in enumerate(nums):
            if elem > 0:
                break

            if idx > 0 and elem == nums[idx-1]:
                continue

            left, right = idx+1, n-1
            while left < right:
                three_sum = elem + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([elem, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while (left < right) and nums[left] == nums[left-1]:
                        left += 1
        
        return res

            