class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []
        n = len(nums)

        def _dfs(start):
            nonlocal res
            xor = 0
            for elem in subset:
                xor ^= elem
            res += xor
            for i in range(start, n):
                subset.append(nums[i])
                _dfs(i + 1)
                subset.pop()

        _dfs(0)
        return res