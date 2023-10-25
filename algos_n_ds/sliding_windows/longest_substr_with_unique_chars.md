# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use a hash map to keep track of the position of the last repeated char, we can also use a set instead of a hash map and remove elements until the position of the last repeated char.

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
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seq = {}
        pointer = 0
        result = 0
        
        for i, ch in enumerate(s):
            if ch in seq and seq[ch] >= pointer:
                result = max(i - pointer, result)
                pointer = seq[ch] + 1
                seq[ch] = i
            else:
                seq[ch] = i
        result = max(len(s) - pointer, result)

        return result     
```