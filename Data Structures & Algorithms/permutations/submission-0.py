class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        perm = []
        path = []
        used = [False] * n

        def _backtrack():
            if len(path) == n:
                perm.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                _backtrack()
                
                used[i] = False
                path.pop()
        _backtrack()
        return perm

            
