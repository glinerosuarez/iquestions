# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use a stack to keep track of seen temperatures
# Approach
<!-- Describe your approach to solving the problem. -->
use a monotonic decreasing stack
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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][1]:
                last = stack.pop()
                result[last[0]] = i - last[0]

            stack.append((i, t))

        return result
        
```