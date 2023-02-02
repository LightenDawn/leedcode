# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
 
# Example 1:
# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# Example 2:
# Input: nums = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.

# Example 3:
# Input: nums = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.


#Solution 1 

# 解題邏輯: 
# 本題邏輯條件:
# 1. 題目的x不一定要出現在列表中，例如: [3, 4, 5] x可為1,2,3,4,5
# 2. x要大於等於x的意思為 列表中的數字大於x的數量 = x的值
# 例如 : 
# List = [3, 4, 5]
# X = 1, Counter = 3  -> X
# X = 2, Counter = 3 -> X
# X = 3, Counter = 3 -> return 3

# 因此作法很簡單，純粹找出list中的最大值，並且用for loop進行尋找是否有符合的值，若有則回傳，無則回傳-1。

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        max_num = max(nums)
        for i in range(1, max_num + 1):
            counter = 0
            for j in nums:
                if j >= i:
                    counter += 1
            if counter == i:
                return i
        return -1


#Solution 2 - (參考)

# 解題邏輯: 
# 先反向排序，再用i去判斷哪個索引大於等於i。

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i
            
# [3,9,7,8,3,8,6,6] -> [9, 8, 8, 7, 6, 6, 3, 3]
# nums[0] > 0 -> i = 0+1
# nums[1] > 1 -> i = 1+1
# nums[2] > 2 -> i = 2+1
# nums[3] > 3 -> i = 3+1
# nums[4] > 4 -> i = 4+1
# nums[5] > 5 -> i = 5+1
# nums[6] > 6 -> x (3>6為錯誤)
# return -1 if i(6) < 8 and i(6) == nums[i](3) else i(6)
