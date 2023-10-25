# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
check in which of the two halves the mid point is (ordered half or unorderd one)

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
        l, r = 0, len(nums) - 1
        result = -1

        while l <= r:
            mid = l + (r - l)//2  # mid will always be inside one of the 2 halfs
            if nums[mid] == target:
                result = mid
                break
            
            if nums[l] <= nums[mid]:
                # mid is inside first ordered half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # mid is inside second ordered half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return result
```