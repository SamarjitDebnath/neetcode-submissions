class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        subset = []
        
        def _dfs(start):
            res.append(subset.copy())

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                _dfs(i + 1)
                subset.pop()

        _dfs(start = 0)
        return res
                