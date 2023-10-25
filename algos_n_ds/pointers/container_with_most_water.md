# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use two pointers initialized to the edges of the array, in each iteration we compute the area and move the pointer with the smaller value towards the center of the array

# Approach
<!-- Describe your approach to solving the problem. -->
use two pointers initialized to the edges of the array, in each iteration we compute the area and move the pointer with the smaller value towards the center of the array

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        result = -1

        while l < r:
            lh, rh = height[l], height[r]
            base = r - l
            if lh >= rh:
                result = max(result, base * rh)
                r -= 1
            else:
                result = max(result, base * lh)
                l += 1

        return result
                
```