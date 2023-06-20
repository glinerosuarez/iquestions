# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
converting a list to a set is a $$O(n)$$ operation

# Approach
<!-- Describe your approach to solving the problem. -->
convert list to set and then consecutive numbers in the set

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                
                longest = max(longest, length)

        return longest

```