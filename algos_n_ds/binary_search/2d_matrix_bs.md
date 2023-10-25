# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
treat the matrix as a sorted list

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(log(n * m))$$ 

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ 

# Code
```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            mid_v = matrix[mid // n][mid % n]
            
            if target < mid_v:
                r = mid - 1
            elif target > mid_v:
                l = mid + 1
            else:
                return True

        return False
        
```