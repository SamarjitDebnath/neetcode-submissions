class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        parentheses_pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        iter_stack = []
        for elem in s:
            if elem in parentheses_pair:
                if iter_stack and iter_stack[-1] == parentheses_pair[elem]:
                    iter_stack.pop()
                else:
                    return False
            else:
                iter_stack.append(elem)
        
        return True if not iter_stack else False
