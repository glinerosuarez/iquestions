# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
the amount of water in each position is equal to min(max_left_height, max_right_height) - height of position

# Approach
<!-- Describe your approach to solving the problem. -->
two pointers, keep updating the opposite side as we see higher values

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        result = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                result += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                result += max_r - height[r]

        return result
```