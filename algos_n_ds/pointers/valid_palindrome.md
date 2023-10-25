# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use left and right pointers, compare values in the pointers ignoring any no alpha numeric value

# Approach
<!-- Describe your approach to solving the problem. -->
use left and right pointers, compare values in the pointers ignoring any no alpha numeric value

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_alnum(s[l]):
                l += 1
            while l < r and not self.is_alnum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def is_alnum(self, ch):
        return (
            ord("A") <= ord(ch) <= ord("Z")
            or ord("a") <= ord(ch) <= ord("z")
            or ord("0") <= ord(ch) <= ord("9")
        )
```