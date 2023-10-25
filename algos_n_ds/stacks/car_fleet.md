# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
order cars by position and compute time to get to the target to get cars that will catch up and merge into a fleet

# Approach
<!-- Describe your approach to solving the problem. -->
order cars by position and compute time to get to the target to get cars that will catch up and merge into a fleet

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(nlogn)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s_pos = sorted(zip(position, speed))
        f = 1
        lt = (target - s_pos[-1][0]) / s_pos[-1][1]
        
        for p, s in s_pos[::-1][1:]:
            tt = (target - p) / s

            if tt > lt:
                f += 1
                lt = tt

        return f


        
        

        
```