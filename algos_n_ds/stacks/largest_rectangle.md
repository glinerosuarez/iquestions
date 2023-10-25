# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
iterate over the heights, put in a stack the rectangles that can be extended, compute the area for the ones that can't

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
    def largestRectangleArea(self, heights: List[int]) -> int: 
        stack = [(0, heights[0])]
        lr = 0

        for i, h in enumerate(heights[1:]):
            i += 1
            if h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while len(stack) > 0 and h < stack[-1][1]:
                    id, height = stack.pop()
                    lr = max(lr, (i - id) * height)
                stack.append((id, h))

        while len(stack) > 0:
            id, height = stack.pop()
            lr = max(lr, (len(heights) - id) * height)
        
        return lr
```