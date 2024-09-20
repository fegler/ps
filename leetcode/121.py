class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        ret = 0 
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                ret = max(ret, prices[i]-min_val)
            else:
                min_val = min(min_val, prices[i])
        return ret