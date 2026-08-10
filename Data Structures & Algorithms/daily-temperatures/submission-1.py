class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # bruteforce - time: O(n^2), space: O(1)
        # res = []
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         count += 1
        #         if temperatures[j] > temperatures[i]:
        #             break
        #     else:
        #         count = 0
        #     res.append(count)
        # return res

        # Monotonic decreasing stack - time: O(n), space: O(n)
        res = [0] * len(temperatures)
        monoticStack = [] # pair: [temperature, index]

        for i, temperature in enumerate(temperatures):
            while monoticStack and monoticStack[-1][0] < temperature:
                stackTemp, stackIdx = monoticStack.pop()
                res[stackIdx] = i - stackIdx
            monoticStack.append([temperature, i])
            
        return res
