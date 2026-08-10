class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        parantheses_pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        pStack = []

        for i in range(len(s)):
            if s[i] in parantheses_pair:
                if pStack and pStack[-1] == parantheses_pair[s[i]]:
                    pStack.pop()
                else:
                    return False
            else:
                pStack.append(s[i])
        
        return True if not pStack else False