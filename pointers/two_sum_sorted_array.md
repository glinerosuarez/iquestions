# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use two pointers, increase left if current sum is smaller than target or decrease right if current sum is bigger than target

# Approach
<!-- Describe your approach to solving the problem. -->
use two pointers, increase left if current sum is smaller than target or decrease right if current sum is bigger than target

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        
        return [l+1, r+1]

```