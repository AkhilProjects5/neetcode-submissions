class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        t = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        INF = float("inf")

        for j in range(1,len(t[0])):
            t[0][j] = INF-1
        
        for j in range(1,len(t[0])):
            if j% coins[0] == 0:
                t[1][j] = j//coins[0]
            else:
                t[1][j] = INF-1

        for i in range(2,len(t)):
            for j in range(1,len(t[0])):
                
                if coins[i-1] <= j:
                    t[i][j] = min(1+ t[i][j-coins[i-1]],t[i-1][j])

                else:
                    t[i][j] = t[i-1][j]
        

        return -1 if t[n][amount] >= INF - 1 else int(t[n][amount])