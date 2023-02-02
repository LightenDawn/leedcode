# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


import bisect

#Solution 1
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 使用陣列二分演算法
        return bisect.bisect_left(nums ,target)


#Solution 2
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            # 如果目標值小於或等於nums的當前索引
            if target <= nums[i]:
                # 目標值應插入的位置為當前位置
                return i
        # 若nums都索引完畢，未找到可插入的位置，代表目標值皆大於nums的值
        # 因此回傳nums的長度為目標值應插入的位置
        return len(nums)


#Solution 3
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 將target插入至nums[0]的位置
        nums.insert(0, target)
        index = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                # 進行排序
                nums[i], nums[i+1] = nums[i+1], nums[i]
                # 紀錄變更的位置
                index += 1
        return index