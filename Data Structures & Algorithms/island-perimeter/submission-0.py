class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        perimeter = 0

        def _dfs(r, c):
            nonlocal perimeter
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return

            grid[r][c] = -1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    _dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    _dfs(r, c)
        return perimeter