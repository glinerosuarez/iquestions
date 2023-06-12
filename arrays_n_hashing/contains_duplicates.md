# Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
```
Input: nums = [1,2,3,1]
Output: true
```
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
sets, iterate over the input list once, keep track of seen elements

# Approach
<!-- Describe your approach to solving the problem. -->
Since checking if an element is in a set takes $$O(1)$$, we can iterate over the input list and use a set to keep track of the elements we've already seen, checking every element at a time.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        else:
            return False

```