# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
find the value in the second array where all smaller elements are smaller than the last number in the first array necessary to complete one half of the two arrays combined

# Approach
<!-- Describe your approach to solving the problem. -->

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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = [float("-inf")] + nums1 + [float("inf")], [float("-inf")] + nums2 + [float("inf")]

        if len(A) < len(B):
            A, B = B, A

        Asize, Bsize = len(A), len(B)
        total = Asize + Bsize
        half_size = total // 2
        
        l, r = 0, Bsize - 1
        while l <= r:
            mid = l + (r - l)//2
            Bhalf_size = mid + 1 # 1
            Ahalf_size = half_size - Bhalf_size # 0

            edge_Ahalf = A[Ahalf_size - 1] # -inf
            edge_Bhalf = B[Bhalf_size - 1] # 2
            next_Ahalf = A[Ahalf_size] # 1 
            next_Bhalf = B[Bhalf_size] # inf
            
            if edge_Ahalf <= next_Bhalf:
                if edge_Bhalf <= next_Ahalf:
                    if total % 2 == 0:
                        return (max(edge_Ahalf, edge_Bhalf) + min(next_Ahalf, next_Bhalf))/2
                    else:
                        return min(next_Ahalf, next_Bhalf)
                else:
                    r = mid - 1
            else:
                l = mid + 1

        return mid
        
```