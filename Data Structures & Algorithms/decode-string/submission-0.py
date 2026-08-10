class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for elem in s:
            if elem == "]":
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                # pop "["
                if stack:
                    stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(substr * int(num))
            else:
                stack.append(elem)
        
        return "".join(stack)