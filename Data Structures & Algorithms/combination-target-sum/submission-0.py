class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def _dfs(start, remaining):
            if remaining < 0:
                return
            
            if remaining == 0:
                res.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                _dfs(i, (remaining - nums[i]))
                subset.pop()

        _dfs(start=0, remaining=target)
        return res