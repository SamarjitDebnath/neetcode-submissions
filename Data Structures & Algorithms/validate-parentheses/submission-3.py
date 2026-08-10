class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        validP = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        pStack = []

        for i in range(len(s)):
            if s[i] in validP:
                if pStack and pStack[-1] == validP[s[i]]:
                    pStack.pop()
                else:
                    return False
            else:
                pStack.append(s[i])
        
        return True if not pStack else False