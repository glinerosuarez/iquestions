# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
hashmap, count characters

# Approach
<!-- Describe your approach to solving the problem. -->
1. counting chars for every word and group words with the same char count
2. sort every word and group

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
1. $$O(n*m*26)$$
2. $$O(n*mlogm)$$
Second approach is more performant for words with an average length < 2^26

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = {} 

        for s in strs:
            counter = [0] * 26  # Total lowercase characters in english
            for c in s:
                counter[ord(c) - ord('a')] += 1
            ac = a.get(tuple(counter), [])
            ac.append(s)
            a[tuple(counter)] = ac
        
        return list(a.values())

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = {}

        for s in strs:
            ss = "".join(sorted(s))
            l = a.get(ss, [])
            l.append(s)
            a[ss] = l

        return list(a.values())
```