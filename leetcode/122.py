class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-1 for _ in range(len(prices)+1)]
        now_min, now_max = prices[0], prices[0]
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                now_max = prices[i]
            else:
                ret += (now_max - now_min)
                now_min, now_max = prices[i], prices[i]
        if now_min != now_max:
            ret += (now_max - now_min)
        return ret