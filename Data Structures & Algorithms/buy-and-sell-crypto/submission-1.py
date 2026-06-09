class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)-1):
        #     if prices[i] > max(prices[i+1:]):
        #         pass
        #     else:
        #         for j in range(i+1,len(prices)):
        #             if prices[j] - prices[i] > profit :
        #                 profit = prices[j]-prices[i]
        
        # return profit

        # -------------------------------------------------

        profit = 0
        i,j = 0,1
        while j < len(prices):
            if prices[j] - prices[i] > profit :
                profit = prices[j] - prices[i]
            
            if prices[j] < prices[i]:
                i = j 
            
            j +=1
        return profit
            
