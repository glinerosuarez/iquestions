class Solution:
    def decodable(self, num: str) -> bool:
        if len(num) == 0 or (len(num) == 2 and num[0] == "0"):
            return 0
        
        num = int(num)
        if 0 < num <= 26:
            return 1
        else:
            return 0

    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        n = len(dp)

        # base case 0
        dp[0] = 1
        dp[1] = self.decodable(s[0])

        for i in range(2, n):
            result = 0
            if self.decodable(s[i-1]) == 1:
                if dp[i-1] > 0:
                    result += dp[i-1]

            if self.decodable(s[i-2:i]) == 1:
                if dp[i-2] > 0:
                    result += dp[i-2]

            dp[i] = result
        
        return dp[-1]

        
