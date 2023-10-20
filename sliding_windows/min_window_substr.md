# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
sliding window, hash maps, matches count variable

# Approach
<!-- Describe your approach to solving the problem. -->
keep track of the count of letters in the current window, every time we find a valid window (with all the required characters) we move left pointer until the window is no longer valid while checking for the optimal value in the process

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        from collections import Counter
        count = Counter(t)
        w_count = {k: 0 for k in count.keys()}
        matches = len(count)
        l = 0
        result = s + " "
        first = False

        for r in range(len(s)):
            char_r = s[r]
            
            if char_r in count:
                w_count[char_r] += 1
                if w_count[char_r] == count[char_r]:
                    matches -= 1
                
                while matches == 0:   
                    result = result if len(s[l:r + 1]) >= len(result) else s[l:r + 1]
          
                    if s[l] in count:
                        w_count[s[l]] -= 1
                        if w_count[s[l]] < count[s[l]]:
                            matches += 1
                    l += 1
                    while l < r and s[l] not in count:
                        l += 1

        return result if len(result) <= len(s) else ""
```