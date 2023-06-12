# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
order characters and their corresponding frequencies, two possible approaches:
1. order both strings and compare
2. build a hashmap with char and frequencies 

# Approach
<!-- Describe your approach to solving the problem. -->
1. order both strings and compare
2. build a hashmap with char and frequencies


# Complexity
- Time complexity: 
1. using ordering: $$O(nlogn)$$
2. using hashmap: $$O(s + t + len(counter))$$ == $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
1. using ordering: $$O(1)$$ assuming input is a list of characters and in-place sorting algorithm.
2. using hashmap: $$O(26 chars at most))$$ == $$O(1)$$

# Code
```
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

class SolutionDict(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 

        counter = {}
        for k in s:
            counter[k] = counter.get(k, 0) + 1

        for k in t:
            counter[k] = counter.get(k, 0) - 1

        for v in counter.values():
            if v != 0:
                return False

        return True
```