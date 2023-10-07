# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use binary search to look for the lowest speed, where the range should be 1 ... max(piles)

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(nlogn + logmax(piles) * n)$$ 
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k
        lh = len(piles)
        
        def eat_bananas(speed):  # returns hours expended
            result = 0
            for p in piles:
                result += (p // speed + bool(p % speed))
            return result
        
        while l <= r:
            mid = l + ((r - l) // 2)
            hours = eat_bananas(mid)
            if hours <= h:
                r = mid - 1
                if hours >= lh:
                    k = mid
                    lh = hours
            elif hours >= lh:
                l = mid + 1
            
        return k        
```