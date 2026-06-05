class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x = prices[0]
        y = prices[0]
        maxval = 0
        for i in range(1, len(prices)):
            y = prices[i]
            if x > prices[i]:
                x = prices[i]
            val = y - x
            maxval = max(maxval, val)
        return maxval
