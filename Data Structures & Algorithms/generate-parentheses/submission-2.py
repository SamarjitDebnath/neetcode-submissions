class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        parentheses = []

        def _generate(opening, closing):
            if opening == closing == n:
                parentheses.append(''.join(stack))

            if opening < n:
                stack.append("(")
                _generate((opening + 1), closing)
                stack.pop()

            if closing < opening:
                stack.append(")")
                _generate(opening, (closing + 1))
                stack.pop()

        _generate(0, 0)
        return parentheses