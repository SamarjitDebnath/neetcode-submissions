class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # brute force
        # res = []

        # def valid(s: str):
        #     opening = 0
        #     for elem in s:
        #         opening += 1 if elem is "(" else -1
        #         if opening < 0:
        #             return False
        #     return not opening

        # def dfs(s: str):
        #     if (2 * n) == len(s):
        #         if valid(s):
        #             res.append(s)
        #         return
        #     dfs(s + "(")
        #     dfs(s + ")")

        # dfs("")
        # return res

        # optimised backtracking
        # add open parenthesis if open < n
        # add closing parenthesis if close < open
        # valid/base condition: open == close == n

        stack = [] # stack for recursion
        res = []

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count+1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count+1)
                stack.pop()
        
        # call the inner function
        backtrack(open_count=0, close_count=0)
        return res