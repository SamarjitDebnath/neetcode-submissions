import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        
        stack = []
        for elem in tokens:
            if elem not in operations:
                stack.append(int(elem))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(operations[elem](num1, num2)))
        
        return stack[0] if stack else -1