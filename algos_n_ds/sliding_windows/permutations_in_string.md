# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use hash maps, sliding window, variable to keep track of matches (counts of the same letter)

# Approach
<!-- Describe your approach to solving the problem. -->
use to hashmaps to keep track of letters and freq, use a matches variables to keep track of equal counts, update second hash map and matches with a slide window 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(length first array * 2)$$

# Code
```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        from collections import Counter
        counter1 = Counter(s1)
        matches = 0

        l = 0
        counter2 = dict(zip(counter1.keys(), [0] * len(counter1)))

        for i in range(len(s1)):
            if s2[i] in counter2:
                counter2[s2[i]] += 1
        for k in counter2.keys():
            if counter1[k] == counter2[k]:
                matches += 1

        if matches == len(counter2):
            return True

        for r in range(i + 1, len(s2)):
            ch = s2[r]
            l += 1
            if s2[l - 1] in counter2:  
                if counter2[s2[l - 1]] == counter1[s2[l - 1]]:
                    matches -= 1
                    counter2[s2[l - 1]] -= 1
                else:
                    counter2[s2[l - 1]] -= 1
                    if counter2[s2[l - 1]] == counter1[s2[l - 1]]:
                        matches += 1
            
            if ch in counter2:
                if counter2[ch] == counter1[ch]:
                    matches -= 1
                    counter2[ch] += 1
                else:
                    counter2[ch] += 1
                    if counter2[ch] == counter1[ch]:
                        matches += 1

            if matches == len(counter2):
                return True
        
        return False
```