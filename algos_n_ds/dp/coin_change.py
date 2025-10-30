class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = [0] + coins
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 0

        for j in range(1, amount + 1):
            dp[0][j] = float("inf")

        for i in range(1, n):
            for c in range(1, amount + 1):
                if c - coins[i] >= 0:
                    dp[i][c] = min(dp[i][c - coins[i]] + 1, dp[i-1][c])
                else:
                    dp[i][c] = dp[i-1][c]

                
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]
            
        
