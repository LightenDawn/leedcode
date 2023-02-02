# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


#Solution 1 - 參考網路 使用Dynamic programming
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 建立長度與nums相等的0列表
        dp = [0] * len(nums)
        if len(nums) <= 1: return max(nums)
        for i in range(len(nums)):
            # 當前索引值取最大值
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        # 取列表中的最大值
        return max(dp)


#Solution 2 - 參考網路
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 與前題類似，但是更精簡
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)