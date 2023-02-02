# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


#Solution 1 - Brute Force
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

solution = Solution()
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)
solution.twoSum([3, 3], 6)


#Solution 2 - Brute Force改寫
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = target
        for i in range(len(nums)):
            temp -= nums[i]
            #如果temp減去當前值後，存在在後續的list中才會進行for-loop
            #加快運行時間
            if temp in nums[i+1:]:
                for j in range(i+1,len(nums)):
                    if nums[j] == temp:
                        return i, j
            temp = target


solution = Solution()
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)
solution.twoSum([3, 3], 6)


#Solution 3 - Hash Map(參考網路)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #是否拜訪過的dict
        seen = {}
        for i, value in enumerate(nums):
            #餘數
            remaining = target - nums[i]
            
            #若餘數有出現在seen字典中
            if remaining in seen:
                #回傳當前位置i和餘數的位置
                return [i, seen[remaining]]
            
            #加入餘數的位置
            seen[value] = i

solution = Solution()
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)
solution.twoSum([3, 3], 6)