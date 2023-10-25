# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
look for the number that we need to solve the equiation n + x = target

# Approach
<!-- Describe your approach to solving the problem. -->
for every number in the array we compute the value that we need to solve the equation n + x = target, then we store the needed value and its corresponding index in a hashmap, for every iteration we check if the value has been previously seen 

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        needed = {}

        for i, n in enumerate(nums):
            if n in needed:
                return [needed[n], i]
            else:
                needed[target - n] = i
```