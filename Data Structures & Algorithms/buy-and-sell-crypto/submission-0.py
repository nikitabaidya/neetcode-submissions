class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            # found profitable 
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l],profit)

            # Found lower price, move buy pointer here
            else:
                l = r

            # Move sell pointer forward
            r += 1

        return profit
                