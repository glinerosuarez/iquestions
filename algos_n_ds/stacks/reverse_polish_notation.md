# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
using a stack

# Approach
<!-- Describe your approach to solving the problem. -->
use a stack

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
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
        
```