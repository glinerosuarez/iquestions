class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [ [0 for _ in range(l)] for _ in range(l)] # l X l
        
        for i in range(l):
            dp[i][i] = 1  # base case on letter

        for length in range(1, l):
            for i in range(l - length):
                j = i + length

                if length == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 2

                if s[i] == s[j]:
                    inner_sub = dp[i + 1][j - 1]
                    if inner_sub > 0:
                        p_length = inner_sub + 2
                        dp[i][j] = p_length

        result = ""
        for i in range(l):
            for j in range(l -1, i - 1, -1):
                p_length = dp[i][j]
                result = s[i:j+1] if p_length > len(result) else result
        return result
                

