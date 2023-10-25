# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use two pointers update buy pointer when we found a smaller value

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while l < len(prices) and r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                result = max(result, prices[r] - prices[l])
                r += 1
        
        return result
```