class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        def _dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0

            # grid[r][c] = 0
            visit.add((r, c))
            res = 1
            for dr, dc in directions:
                res += _dfs((r + dr), (c + dc))

            return res
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, _dfs(r, c))
        return area