class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        next_warmer = [0] * n
        
        stack = [] # store tuple (temperature, index)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, i = stack.pop()
                next_warmer[i] = idx - i
            stack.append((temp, idx))

        return next_warmer