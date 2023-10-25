# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
split every operation in multiplication of elemtents to the left times the multiplication of elements to the right

# Approach
<!-- Describe your approach to solving the problem. -->
compute posfix for every element (multiply all elements to the righ)
compute prefix for every element (multiply all elements to the left)
multiply both parts


# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        result = [1] * N

        for i in range(N-1,0,-1):
            result[i-1] = nums[i] * result[i]

        prefix = 1
        for i in range(N):
            result[i] = result[i] * prefix
            prefix = prefix * nums[i] 

        return result

        

        

```