# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
1. hashmap, sorting, max heap
2. bucket sorting, hashmap

# Approach
<!-- Describe your approach to solving the problem. -->
1. store frequencies in a hashmap and then sort by frequency to get the top k values (we can usea a max heap too)
2. Use bucket sorting, compute frequencies in a hash map, set all possible frequencies as buckets and assign each number to its corresponding bucket, iterate over the buckets until we get k elements.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
1. $$O(n+mlogm)$$ where m is the number of distinct values
2. $$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
1. $$O(n)$$
2. $$O(n)$$

# Code
```
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        c = {}
        order = []

        for n in nums:
            c[n] = c.get(n, 0) + 1

        return map(lambda x: x[0], sorted(c.items(), key=lambda x: x[1], reverse=True))[:k]
        

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        c = {}
        order = []

        for n in nums:
            c[n] = c.get(n, 0) + 1

        return map(lambda x: x[0], sorted(c.items(), key=lambda x: x[1], reverse=True))[:k]
        
        buckets = [[] for _ in range(len(nums))]
        freq = {}
        result = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for key, v in freq.items():
            buckets[v -1].append(key)

        for i in range(len(nums)):
            bucket = buckets[-(i+1)]
            for e in bucket:
                result.append(e)
                if len(result) == k:
                    return result
            
```