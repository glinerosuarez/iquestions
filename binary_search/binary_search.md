# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
binary search algo

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logn)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$
# Code
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """def fun(ids: List[int], target: int):
            if len(ids) == 1:
                return -1 if nums[ids[0]] != target else ids[0]

            l, r = 0, int(len(ids) / 2)

            if target == nums[ids[r]]:
                return ids[r]
            elif target < nums[ids[r]]:
                return fun(ids[:r], target)
            else:
                return fun(ids[r:], target)

        return fun(list(range(len(nums))), target)"""


        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2) 
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1 
            else:
                l = mid + 1
        
        return -1
```