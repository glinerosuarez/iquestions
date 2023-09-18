# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use a stack

# Approach
<!-- Describe your approach to solving the problem. -->
compare the last element in the stack while iterating over the string

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
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in mappings:
                stack.append(c)
            elif len(stack) > 0:
                last = stack.pop()
                if mappings[last] != c:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False


```