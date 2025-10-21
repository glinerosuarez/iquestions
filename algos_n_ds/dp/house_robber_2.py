class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # evaluate house in pos 0
        # if it is part of the optimal solution then we solve:
        nums_is = [0] + nums[2:-1]
        N_is = len(nums_is)
        dp_is = [0] * N_is

        if N_is > 1:        
            dp_is[1] = nums_is[1]

        for i in range(2, N_is):
            dp_is[i] = max(dp_is[i - 1], dp_is[i - 2] + nums_is[i])
        
        # if it is not then
        nums_n = [0] + nums[1:]
        N_n = len(nums_n)
        dp_n = [0] * N_n   
        if N_n > 1:        
            dp_n[1] = nums_n[1]

        for i in range(2, N_n):
            dp_n[i] = max(dp_n[i - 1], dp_n[i - 2] + nums_n[i])
        
        return max(nums[0] + dp_is[-1], dp_n[-1])
        
