# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
order array, iterate over distinct numbers, apply 2sum algo for each iteration
# Approach
<!-- Describe your approach to solving the problem. -->
order array, iterate over distinct numbers, apply 2sum algo for each iteration
# Complexity
- Time complexity: $$O(nlogn)$$ + $$O(n^2)$$ = $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        a_last_value = None

        for a, v in enumerate(nums[:-2]):
            if v == a_last_value:
                continue
            
            b, c = a + 1, len(nums) - 1
            b_last_value = None
            while b < c:
                if nums[b] == b_last_value:
                    b +=1
                    continue

                if v + nums[b] + nums[c] == 0:
                    result.append([v, nums[b], nums[c]])
                    a_last_value, b_last_value = v, nums[b]
                    b += 1
                    c -= 1
                elif v + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    b += 1

            a_last_value = v
        
        return result

    


            

```