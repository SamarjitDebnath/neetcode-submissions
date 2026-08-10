class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def _dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or word[i] != board[r][c]
                or board[r][c] == "#"):
                return False

            board[r][c] = "#"
            isword = (
                _dfs((r - 1), c, (i + 1))
                or _dfs((r + 1), c, (i + 1))
                or _dfs(r, (c - 1), (i + 1))
                or _dfs(r, (c + 1), (i + 1))
            )
            board[r][c] = word[i]
            return isword

        for r in range(ROWS):
            for c in range(COLS):
                if _dfs(r, c, 0):
                    return True
        
        return False

