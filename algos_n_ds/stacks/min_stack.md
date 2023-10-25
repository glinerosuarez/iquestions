# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
consider each node having a corresponding min value in that position

# Approach
<!-- Describe your approach to solving the problem. -->
consider each node having a corresponding min value in that position

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```
class MinStack:

    def __init__(self):
        self.stack = []
        self.order = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            self.order.append(min(val, self.order[-1]))
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.order.append(val)
        

    def pop(self) -> None:
        self.order.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.order[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```