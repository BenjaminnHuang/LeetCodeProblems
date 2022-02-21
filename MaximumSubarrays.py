class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxi = nums[0]
        
        for i in range(len(nums))[1:]:
            nums[i] = max(nums[i], (nums[i] + nums[i-1]) )
            maxi = max(nums[i], maxi)
        return maxi
        