class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[float("inf") for _ in range(k)] for _ in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = i

        for j in range(k):
            dp[0][j] = 0
            dp[1][j] = 1

        for j in range(1, k):
            for i in range(2, n + 1):
                for x in range(1, i+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-x][j], dp[x-1][j-1]))
                    
        return dp[-1][-1]

        
