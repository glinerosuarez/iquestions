# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
sliding window, hash map, max frequency

# Approach
<!-- Describe your approach to solving the problem. -->
iterate over the array while expanding the window until it's no longer valid according to the equation w_size - maxf <= k for a valid window, keep in mind that to find and optimal solution we only care about finding bigger values of maxf.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(26)$$

# Code
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = maxf = result = 0
        counter = {}

        while l < len(s) and r < len(s):
            w_size = r - l + 1
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxf = max(counter[s[r]], maxf)
            #maxf = max(counter.values())
            if w_size - maxf <= k:
                result = max(result, w_size)
            else:
                counter[s[l]] -= 1
                l += 1
            r += 1

        return result  
        
```