# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
there are two sorted parts, decide in which part the mid point is

# Approach
<!-- Describe your approach to solving the problem. -->
return nums[l] if the two pointers are inside of one of the two sorted parts or nums[mid] if mid is the smallest value

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(logn)$$
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$ 
# Code
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_i = len(nums) - 1
        l, r = 0, last_i
        res = nums[last_i]

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            
            mid = l + ((r - l) // 2)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
```