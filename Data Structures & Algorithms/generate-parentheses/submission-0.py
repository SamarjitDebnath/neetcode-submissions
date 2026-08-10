class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            opening = 0
            for elem in s:
                opening += 1 if elem is "(" else -1
                if opening < 0:
                    return False
            return not opening

        def dfs(s: str):
            if (2 * n) == len(s):
                if valid(s):
                    res.append(s)
                return
            dfs(s + "(")
            dfs(s + ")")

        dfs("")
        return res