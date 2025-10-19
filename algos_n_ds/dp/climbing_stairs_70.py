class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * (n + 1)
        if n < 3:
            return n

        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
