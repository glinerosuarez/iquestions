# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
pass the length of each word together with a delimiter

# Approach
<!-- Describe your approach to solving the problem. -->
pass the length of each word together with a delimiter

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        words = []
        i = 0
        while i < len(str):
            ch_length = ""
            for j in range(i, len(str)):
                if str[j] == "#":
                    words.append(str[j+1:j+1+int(ch_length)])
                    i = j+1+int(ch_length)
                    break
                else:
                    ch_length += str[j]
        
        return words
```