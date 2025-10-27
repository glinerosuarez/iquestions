class Solution:
    
    def construct_is_palindrome(self, s: str):
        dp_is_palindrome = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp_is_palindrome[i][i] = True

        for i in range(0, len(s) - 1):
            dp_is_palindrome[i][i+1] = s[i] == s[i+1]

        for length in range(2, len(s)):
            for i in range(len(s) - length):
                j = i + length
                dp_is_palindrome[i][j] = dp_is_palindrome[i+1][j-1] and s[i] == s[j]
        
        return dp_is_palindrome

    def countSubstrings(self, s: str) -> int:
        dp_is_palindrome = self.construct_is_palindrome(s)
        dp = [None] * len(s)        
        dp[0] = 1
        
        for i in range(1, len(s)):
            count = 0
            j = i
            while j >= 0:
                if dp_is_palindrome[j][i]:
                    count += 1
                j -= 1
                
            dp[i] = count + dp[i-1]
        
        return dp[len(s) - 1]
        
