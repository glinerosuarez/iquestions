class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        opt_max = [None] * n
        opt_min = [None] * n

        result = opt_max[0] = opt_min[0] = nums[0]

        for i in range(1, n):
            v = nums[i]
            opt_max[i] = max(v, opt_max[i-1]*v, opt_min[i-1]*v)
            opt_min[i] = min(v, opt_max[i-1]*v, opt_min[i-1]*v)
            result = max(result, opt_max[i])

        return result
