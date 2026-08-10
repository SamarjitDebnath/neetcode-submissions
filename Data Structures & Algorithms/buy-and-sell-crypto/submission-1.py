class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bruteforce: O(n^2)
        # _maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = max(maxProfit, (prices[j]-prices[i]))

        # return _maxProfit

        l, r = 0, 1
        _maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                _maxProfit = max(_maxProfit, (prices[r]-prices[l]))
            else:
                l = r
            r += 1
        return _maxProfit

