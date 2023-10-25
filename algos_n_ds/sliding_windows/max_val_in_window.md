# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
deque, sliding window

# Approach
<!-- Describe your approach to solving the problem. -->
deque to keep track of next max value, so deque is gonna be monotonically decreasing

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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        l = 0
        result = []

        for r in range(len(nums)):
            #print(deque, result, l)
            n = nums[r]
            #if len(deque) == 0:
            #    deque.append(n)
            #else:
            while len(deque) > 0 and deque[-1] < n:
                deque.pop()
            deque.append(n)
            
            if r >= k - 1:
                result.append(deque[0])
                if nums[l] == deque[0]:
                    deque.popleft()
                l += 1

        return result 
```